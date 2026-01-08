import os
from flask import (
    Flask, render_template, redirect, url_for,
    request, session, flash, jsonify
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

# -------------------- Load Environment Variables --------------------
load_dotenv()

# -------------------- App Setup --------------------
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev_secret")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# -------------------- Models --------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_subscribed = db.Column(db.Boolean, default=False)

# -------------------- Helper --------------------
def current_user():
    if 'user_id' in session:
        return User.query.get(session['user_id'])
    return None

# -------------------- Health --------------------
@app.route('/health')
def health():
    return "App is running ✅"

# -------------------- Auth Routes --------------------
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
            flash(f"Welcome back, {user.email}!", "success")
            return redirect(url_for('dashboard'))
        flash("Invalid email or password.", "danger")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('index'))

# -------------------- Dashboard --------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    user = current_user()
    if not user:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=user)

# -------------------- Courses & Modules --------------------
courses = {
    "Data Science": {
        "title": "Data Science",
        "icon": "📊",
        "overview": "Learn data cleaning, visualization, and machine learning with real-world datasets.",
        "description": "Learn fundamentals of data analysis, visualization, and machine learning.",
        "modules": [{"id": i, "title": f"Data Science Module {i}", "description": f"Content for Data Science Module {i}"} for i in range(1, 16)]
    },
    "Statistics": {
        "title": "Statistics",
        "icon": "📈",
        "overview": "Master probability, inference, and modeling for data-driven decision making.",
        "description": "Master probability, inference, and statistical modeling techniques.",
        "modules": [{"id": i, "title": f"Statistics Module {i}", "description": f"Content for Statistics Module {i}"} for i in range(1, 16)]
    },
    "R Programming": {
        "title": "R Programming",
        "icon": "💻",
        "overview": "Build reproducible workflows and dashboards using R and the tidyverse.",
        "description": "Build reproducible workflows and powerful analytics with R.",
        "modules": [{"id": i, "title": f"R Programming Module {i}", "description": f"Content for R Programming Module {i}"} for i in range(1, 16)]
    }
}

@app.route('/course/<string:name>')
def course(name):
    user = current_user()
    if not user:
        return redirect(url_for('login'))

    course = courses.get(name)
    if not course:
        flash("Course not found.", "danger")
        return redirect(url_for('dashboard'))

    return render_template('course.html', course=course, user=user)

@app.route('/module/<string:course_name>/<int:id>')
def module(course_name, id):
    user = current_user()
    if not user:
        return redirect(url_for('login'))

    course = courses.get(course_name)
    if not course:
        flash("Course not found.", "danger")
        return redirect(url_for('dashboard'))

    module_data = next((m for m in course["modules"] if m["id"] == id), None)
    if not module_data:
        flash("Module not found.", "danger")
        return redirect(url_for('course', name=course_name))

    if not user.is_subscribed and id > 5:
        flash("This module is locked. Please subscribe to unlock.", "warning")
        return redirect(url_for('course', name=course_name))

    return render_template("module.html", module=module_data, course=course, user=user)

# -------------------- PayPal Hosted Buttons --------------------
# Hosted Button IDs from your PayPal dashboard
MODULE_BUTTON_ID = "25ZB5B5M2Z9F8"   # single module unlock
COURSE_BUTTON_ID = "E4QRSZMBN6Q4E"   # full course unlock

@app.route('/unlock-module')
def unlock_module():
    user = current_user()
    if not user:
        flash("Login required to unlock modules.", "danger")
        return redirect(url_for('login'))
    return render_template("unlock_module.html", hosted_button_id=MODULE_BUTTON_ID, user=user)

@app.route('/unlock-course')
def unlock_course():
    user = current_user()
    if not user:
        flash("Login required to unlock courses.", "danger")
        return redirect(url_for('login'))
    return render_template("unlock_course.html", hosted_button_id=COURSE_BUTTON_ID, user=user)

@app.route('/paypal-success')
def paypal_success():
    user = current_user()
    if user:
        user.is_subscribed = True
        db.session.commit()
    flash("PayPal payment successful. Subscription activated.", "success")
    return redirect(url_for('dashboard'))

@app.route('/paypal-cancel')
def paypal_cancel():
    flash("PayPal payment cancelled.", "warning")
    return redirect(url_for('dashboard'))

# -------------------- Run App --------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
