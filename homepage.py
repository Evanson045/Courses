import os
import requests
import logging
from flask import (
    Flask, render_template, redirect, url_for,
    request, session, flash, jsonify, abort
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

# -------------------- Load Environment --------------------
load_dotenv()

# -------------------- App Setup --------------------
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev_secret")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///users.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# -------------------- Logging --------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -------------------- Models --------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_subscribed = db.Column(db.Boolean, default=False)

# -------------------- Helpers --------------------
def current_user():
    if 'user_id' in session:
        return User.query.get(session['user_id'])
    return None

# -------------------- Import Courses --------------------
from courses import courses

# -------------------- Health --------------------
@app.route('/health')
def health():
    return "App is running ✅"

# -------------------- Auth Routes --------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form['email'].strip().lower()
        password = request.form['password']
        confirm = request.form.get('confirm_password')

        if not email or not password or not confirm:
            flash("All fields are required.", "danger")
            return redirect(url_for('register'))

        if password != confirm:
            flash("Passwords do not match.", "danger")
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash("Email already registered. Please log in.", "warning")
            return redirect(url_for('login'))

        hashed_pw = generate_password_hash(password)
        new_user = User(email=email, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful. Please log in.", "success")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email'].strip().lower()
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        flash("Invalid email or password.", "danger")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    user = current_user()
    if not user:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=user)

# -------------------- Course Routes --------------------
@app.route('/courses')
def list_courses():
    user = current_user()
    return render_template('courses.html', courses=courses, user=user)

@app.route('/course/<course_name>')
def show_course(course_name):
    course = courses.get(course_name)
    if not course:
        abort(404)
    return render_template('course_detail.html', course=course, course_name=course_name, user=current_user())

@app.route('/courses/<course_name>/chapter/<int:id>')
def show_chapter(course_name, id):
    user = current_user()
    course = courses.get(course_name)
    if not course:
        flash("Course not found.", "danger")
        return redirect(url_for('list_courses'))

    # Guard: user must be logged in to access locked chapters
    if not user and id > 5:
        flash("Please log in to access locked chapters.", "warning")
        return redirect(url_for('login'))

    # Block access to chapters 6–15 if not subscribed
    if user and not user.is_subscribed and id > 5:
        flash("This chapter is locked. Please unlock to continue.", "warning")
        return redirect(url_for('show_course', course_name=course_name))

    # Handle both 'chapters' and 'modules'
    chapter_list = course.get("chapters") or course.get("modules")
    chapter_data = next((c for c in chapter_list if c["id"] == id), None)
    if not chapter_data:
        flash("Chapter not found.", "danger")
        return redirect(url_for('show_course', course_name=course_name))

    return render_template("chapter.html", chapter=chapter_data, course=course, user=user, course_name=course_name)

@app.route('/unlock-chapter/<course_name>/<int:chapter_id>', methods=['GET'])
def unlock_chapter(course_name, chapter_id):
    user = current_user()
    course = courses.get(course_name)
    if not course:
        flash("Course not found.", "danger")
        return redirect(url_for('list_courses'))

    if not user:
        flash("Login required to unlock chapters.", "danger")
        return redirect(url_for('login'))

    if chapter_id <= 5:
        flash("This chapter is already available.", "info")
        return redirect(url_for('show_chapter', course_name=course_name, id=chapter_id))

    flash("This chapter is locked. Please unlock all to continue.", "warning")
    return redirect(url_for('show_course', course_name=course_name))

@app.route('/unlock-all', methods=['POST'])
def unlock_all():
    user = current_user()
    if not user:
        flash("Login required to unlock all.", "danger")
        return redirect(url_for('login'))

    if not user.is_subscribed:
        user.is_subscribed = True
        db.session.commit()
        flash("All courses unlocked successfully! 🎉", "success")
    else:
        flash("You already have access to all courses.", "info")

    return redirect(url_for('dashboard'))

# -------------------- PayPal Config --------------------
PAYPAL_API_BASE = os.getenv("PAYPAL_API_BASE", "https://api-m.paypal.com")  # Go live default
PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID", "")
PAYPAL_SECRET = os.getenv("PAYPAL_SECRET", "")

@app.route('/paypal-success', methods=['POST'])
def paypal_success():
    user = current_user()
    if not user:
        return jsonify({"error": "Not logged in"}), 403

    if not request.is_json:
        return jsonify({"error": "Invalid request format"}), 400

    data = request.get_json(silent=True) or {}
    order_id = data.get("orderID")
    if not order_id:
        return jsonify({"error": "Missing orderID"}), 400

    # Step 1: Get access token
    try:
        auth_response = requests.post(
            f"{PAYPAL_API_BASE}/v1/oauth2/token",
            headers={"Accept": "application/json"},
            data={"grant_type": "client_credentials"},
            auth=(PAYPAL_CLIENT_ID, PAYPAL_SECRET),
            timeout=10
        )
        auth_response.raise_for_status()
        access_token = auth_response.json().get("access_token")
        if not access_token:
            return jsonify({"error": "Failed to obtain access token"}), 502
    except requests.RequestException as e:
        logger.error(f"PayPal auth failed: {e}")
        return jsonify({"error": f"Auth request failed: {e}"}), 502

    # Step 2: Verify order
    try:
        order_response = requests.get(
            f"{PAYPAL_API_BASE}/v2/checkout/orders/{order_id}",
            headers={"Authorization": f"Bearer {access_token}", "Accept": "application/json"},
            timeout=10
        )
        order_response.raise_for_status()
        order_data = order_response.json()
    except requests.RequestException as e:
        logger.error(f"Order verification failed: {e}")
        return jsonify({"error": f"Order verification failed: {e}"}), 502

    # Step 3: Check status
    if order_data.get("status") == "COMPLETED":
        user.is_subscribed = True
        db.session.commit()
        return jsonify({"status": "ok", "message": "Payment verified. All courses unlocked!"})
    else:
        return jsonify({"error": "Payment not completed"}), 400

# -------------------- Run App --------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
