import os
import requests
import logging
from flask import (
    Flask, render_template, redirect, url_for,
    request, session, flash, jsonify, abort
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.pool import NullPool
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.middleware.proxy_fix import ProxyFix
from dotenv import load_dotenv

# -------------------- Load Environment --------------------
load_dotenv()

# -------------------- Logging --------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -------------------- App Setup --------------------
app = Flask(__name__)

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY environment variable not set")

app.secret_key = SECRET_KEY
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Secure session cookies
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

# -------------------- Database Configuration --------------------
db_url = os.getenv("DATABASE_URL")

if db_url:
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_pre_ping": True,
        "poolclass": NullPool,
        "connect_args": {"sslmode": "require"},
    }
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

logger.info(f"Active DB: {app.config['SQLALCHEMY_DATABASE_URI']}")

# -------------------- PayPal Configuration --------------------
PAYPAL_API_BASE = os.getenv("PAYPAL_API_BASE", "https://api-m.paypal.com")
PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
PAYPAL_SECRET = os.getenv("PAYPAL_SECRET")

# -------------------- Models --------------------
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    is_subscribed = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# -------------------- Helpers --------------------
def current_user():
    uid = session.get("user_id")
    return User.query.get(uid) if uid else None

# -------------------- Import Courses --------------------
from courses import courses

# -------------------- Routes --------------------
@app.route("/health")
def health():
    return "App is running ✅"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"].lower().strip()
        password = request.form["password"]
        confirm = request.form["confirm_password"]

        if password != confirm:
            flash("Passwords do not match", "danger")
            return redirect(url_for("register"))

        if User.query.filter_by(email=email).first():
            flash("Email already registered", "warning")
            return redirect(url_for("register"))

        user = User(email=email)
        user.set_password(password)

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash("Database error, please try again.", "danger")
            return redirect(url_for("register"))

        flash("Account created successfully. Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].lower().strip()
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session["user_id"] = user.id
            return redirect(url_for("dashboard"))

        flash("Invalid credentials", "danger")
        return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logged out successfully.", "info")
    return redirect(url_for("index"))

@app.route("/dashboard")
def dashboard():
    user = current_user()
    if not user:
        return redirect(url_for("login"))
    return render_template("dashboard.html", user=user)

@app.route("/courses")
def list_courses():
    return render_template(
        "courses.html",
        courses=courses,
        user=current_user()
    )

@app.route("/course/<course_name>")
def show_course(course_name):
    user = current_user()
    if not user:
        flash("You need to log in to continue.", "warning")
        return redirect(url_for("login"))

    course = courses.get(course_name)
    if not course:
        abort(404)

    chapters = course.get("chapters") or course.get("modules") or []
    return render_template(
        "course_detail.html",
        course=course,
        course_name=course_name,
        chapter_list=chapters,
        user=user,
        PAYPAL_CLIENT_ID=PAYPAL_CLIENT_ID,
    )

@app.route("/courses/<course_name>/chapter/<int:chapter_id>")
def show_chapter(course_name, chapter_id):
    user = current_user()
    course = courses.get(course_name)
    if not user:
        flash("You need to log in to continue.", "warning")
        return redirect(url_for("login"))
    if not course:
        abort(404)

    chapters = course.get("chapters") or course.get("modules") or []
    chapter = next((c for c in chapters if c.get("id") == chapter_id), None)

    if not chapter:
        abort(404)

    return render_template(
        "chapter.html",
        chapter=chapter,
        course=course,
        user=user,
        course_name=course_name,
        chapter_list=chapters,
        PAYPAL_CLIENT_ID=PAYPAL_CLIENT_ID,
    )

@app.route("/unlock-all", methods=["POST"])
def unlock_all():
    user = current_user()
    if not user:
        return redirect(url_for("login"))
    if not user.is_subscribed:
        user.is_subscribed = True
        db.session.commit()
        flash("All courses unlocked 🎉", "success")
    else:
        flash("Already unlocked.", "info")

    return redirect(url_for("dashboard"))

@app.route("/subscribe")
def subscribe():
    return render_template(
        "subscribe.html",
        user=current_user(),
        PAYPAL_CLIENT_ID=PAYPAL_CLIENT_ID,
    )

# -------------------- PayPal Callback --------------------
@app.route("/paypal-success", methods=["POST"])
def paypal_success():
    user = current_user()
    if not user or not request.is_json:
        return jsonify({"error": "Unauthorized"}), 403

    order_id = request.json.get("orderID")
    if not order_id:
        return jsonify({"error": "Missing orderID"}), 400

    try:
        token_res = requests.post(
            f"{PAYPAL_API_BASE}/v1/oauth2/token",
            data={"grant_type": "client_credentials"},
            auth=(PAYPAL_CLIENT_ID, PAYPAL_SECRET),
            timeout=10,
        )
        token_res.raise_for_status()
        access_token = token_res.json()["access_token"]

        order_res = requests.get(
            f"{PAYPAL_API_BASE}/v2/checkout/orders/{order_id}",
            headers={"Authorization": f"Bearer {access_token}"},
            timeout=10,
        )
        order_res.raise_for_status()
        order_data = order_res.json()

        if (order_data.get("status") == "COMPLETED" and
            order_data["purchase_units"][0]["amount"]["value"] == "25.00"):
            user.is_subscribed = True
            db.session.commit()
            logger.info("User %s subscribed successfully", user.email)
            # Return success so frontend clears PayPal container and hides modal
            return jsonify({"status": "ok"})

    except Exception as e:
        logger.error(f"PayPal verification failed: {e}")

    return jsonify({"error": "Payment verification failed"}), 400

# -------------------- Run --------------------
if __name__ == "__main__":
    app.run(debug=True)
