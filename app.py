import os
import base64
import requests
from datetime import datetime
from flask import (
    Flask, render_template, redirect, url_for,
    request, session, flash, jsonify
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv   # <-- import dotenv at the top

# -------------------- Load Environment Variables --------------------
load_dotenv()  # this loads variables from .env

# -------------------- App Setup --------------------
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev_secret")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# -------------------- M-Pesa Config --------------------
MPESA_CONSUMER_KEY = os.getenv("MPESA_CONSUMER_KEY")
MPESA_CONSUMER_SECRET = os.getenv("MPESA_CONSUMER_SECRET")
MPESA_SHORTCODE = os.getenv("MPESA_SHORTCODE")
MPESA_PASSKEY = os.getenv("MPESA_PASSKEY")
MPESA_CALLBACK_URL = os.getenv("MPESA_CALLBACK_URL")

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

# -------------------- Auth Routes --------------------
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form['email'].strip().lower()
        password = request.form['password']
        confirm = request.form.get('confirm_password')

        if password != confirm:
            flash("Passwords do not match.", "danger")
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash("Email already registered.", "warning")
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

# -------------------- M-Pesa Payment Routes --------------------
@app.route('/mpesa-pay-course/<string:course_name>', methods=['POST'])
def mpesa_pay_course(course_name):
    user = current_user()
    if not user:
        return jsonify({"success": False, "message": "Login required"}), 403

    phone = request.form.get('phone')
    amount = 500  # Example: KES 500 per course

    # TODO: Integrate with M-Pesa Daraja API
    flash(f"Payment request sent for {course_name}. Amount: KES {amount}", "info")

    user.is_subscribed = True
    db.session.commit()
    return redirect(url_for('course', name=course_name))

@app.route('/mpesa-pay-module/<string:course_name>/<int:id>', methods=['POST'])
def mpesa_pay_module(course_name, id):
    user = current_user()
    if not user:
        return jsonify({"success": False, "message": "Login required"}), 403

    phone = request.form.get('phone')
    amount = 50  # Example: KES 50 per module

    # TODO: Integrate with M-Pesa Daraja API
    flash(f"Payment request sent for {course_name} - Module {id}. Amount: KES {amount}", "info")

    # For demo: mark user as subscribed globally
    user.is_subscribed = True
    db.session.commit()
    return redirect(url_for('module', course_name=course_name, id=id))

# -------------------- Run App --------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
