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
            # Removed explicit welcome note here
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
        "description": "Learn fundamentals of data analysis, visualization, and machine learning.",
        "modules": [
            {"id": 1, "title": "Introduction to Data Science", "description": "Overview of the field and applications", "free": True},
            {"id": 2, "title": "Understanding Data Types & Structures", "description": "Numeric, categorical, and text data", "free": True},
            {"id": 3, "title": "Data Cleaning Basics", "description": "Handle missing values and tidy datasets", "free": True},
            {"id": 4, "title": "Exploratory Data Analysis (EDA)", "description": "Summarize and visualize datasets", "free": True},
            {"id": 5, "title": "Data Visualization with Matplotlib & Seaborn", "description": "Create charts and plots", "free": True},
            {"id": 6, "title": "Feature Engineering Techniques", "description": "Transform raw data into useful features", "free": False},
            {"id": 7, "title": "Introduction to Machine Learning", "description": "Basic ML concepts and workflows", "free": False},
            {"id": 8, "title": "Supervised Learning: Regression Models", "description": "Linear and advanced regression", "free": False},
            {"id": 9, "title": "Supervised Learning: Classification Models", "description": "Logistic regression, decision trees", "free": False},
            {"id": 10, "title": "Unsupervised Learning: Clustering", "description": "K-means and hierarchical clustering", "free": False},
            {"id": 11, "title": "Model Evaluation & Validation", "description": "Cross-validation, metrics", "free": False},
            {"id": 12, "title": "Handling Big Data with Pandas & Spark", "description": "Large-scale data processing", "free": False},
            {"id": 13, "title": "Advanced Visualization with Plotly", "description": "Interactive dashboards", "free": False},
            {"id": 14, "title": "Deep Learning Foundations", "description": "Neural networks basics", "free": False},
            {"id": 15, "title": "Capstone Project: End-to-End Workflow", "description": "Complete DS project", "free": False},
        ]
    },
    "Statistics": {
        "title": "Statistics",
        "icon": "📈",
        "description": "Master probability, inference, and statistical modeling techniques.",
        "modules": [
            {"id": 1, "title": "Introduction to Statistics", "description": "Basic concepts and importance", "free": True},
            {"id": 2, "title": "Descriptive Statistics & Summaries", "description": "Mean, median, mode, variance", "free": True},
            {"id": 3, "title": "Probability Fundamentals", "description": "Rules and applications of probability", "free": True},
            {"id": 4, "title": "Random Variables & Distributions", "description": "Discrete and continuous distributions", "free": True},
            {"id": 5, "title": "Sampling & Data Collection", "description": "Methods of sampling", "free": True},
            {"id": 6, "title": "Hypothesis Testing Basics", "description": "Null and alternative hypotheses", "free": False},
            {"id": 7, "title": "Confidence Intervals & Estimation", "description": "Interval estimation methods", "free": False},
            {"id": 8, "title": "Correlation & Regression Analysis", "description": "Relationships between variables", "free": False},
            {"id": 9, "title": "ANOVA & Comparing Groups", "description": "Analysis of variance", "free": False},
            {"id": 10, "title": "Nonparametric Methods", "description": "Tests without distribution assumptions", "free": False},
            {"id": 11, "title": "Bayesian Statistics Introduction", "description": "Bayes theorem and applications", "free": False},
            {"id": 12, "title": "Multivariate Statistics", "description": "Multiple variables analysis", "free": False},
            {"id": 13, "title": "Time Series Analysis", "description": "Forecasting and trends", "free": False},
            {"id": 14, "title": "Statistical Modeling in Practice", "description": "Applied modeling techniques", "free": False},
            {"id": 15, "title": "Capstone Project: Statistical Report", "description": "Complete statistical analysis project", "free": False},
        ]
    },
    "R Programming": {
        "title": "R Programming",
        "icon": "💻",
        "description": "Build reproducible workflows and powerful analytics with R.",
        "modules": [
            {"id": 1, "title": "Introduction to R & RStudio", "description": "Getting started with R environment", "free": True},
            {"id": 2, "title": "Data Types & Structures in R", "description": "Vectors, lists, data frames", "free": True},
            {"id": 3, "title": "Importing & Cleaning Data in R", "description": "Read and clean datasets", "free": True},
            {"id": 4, "title": "Data Manipulation with dplyr", "description": "Filter, group, summarize data", "free": True},
            {"id": 5, "title": "Data Visualization with ggplot2", "description": "Create plots and charts", "free": True},
            {"id": 6, "title": "Writing Functions & Modular Code", "description": "Reusable R functions", "free": False},
            {"id": 7, "title": "Control Structures & Iteration", "description": "Loops and conditionals", "free": False},
            {"id": 8, "title": "Statistical Analysis in R", "description": "Basic statistical tests", "free": False},
            {"id": 9, "title": "Working with Dates & Strings", "description": "Handle date-time and text data", "free": False},
            {"id": 10, "title": "Data Reshaping with tidyr", "description": "Tidy data principles", "free": False},
            {"id": 11, "title": "Advanced Visualization Techniques", "description": "Interactive plots", "free": False},
            {"id": 12, "title": "Introduction to Shiny Apps", "description": "Build web apps with R", "free": False},
            {"id": 13, "title": "R Markdown for Reporting", "description": "Dynamic documents", "free": False},
            {"id": 14, "title": "Package Development Basics", "description": "Create R packages", "free": False},
            {"id": 15, "title": "Capstone Project: R Analysis", "description": "Complete data analysis project in R", "free": False},
        ]
    }
}

# -------------------- Course Routes --------------------
@app.route('/courses')
def list_courses():
    user = current_user()
    return render_template('courses.html', courses=courses, user=user)

@app.route('/courses/<course_name>')
def course_detail(course_name):
    user = current_user()
    course = courses.get(course_name)
    if not course:
        flash("Course not found.", "danger")
        return redirect(url_for('list_courses'))
    return render_template('course_detail.html', course=course, course_name=course_name, user=user)

@app.route('/module/<course_name>/<int:id>')
def module(course_name, id):
    user = current_user()
    if not user:
        flash("Login required to access modules.", "danger")
        return redirect(url_for('login'))

    course = courses.get(course_name)
    if not course:
        flash("Course not found.", "danger")
        return redirect(url_for('list_courses'))

    module_data = next((m for m in course["modules"] if m["id"] == id), None)
    if not module_data:
        flash("Module not found.", "danger")
        return redirect(url_for('course_detail', course_name=course_name))

    if not user.is_subscribed and not module_data.get("free", False):
        flash("This module is locked. Please subscribe to unlock.", "warning")
        return redirect(url_for('unlock_module'))

    return render_template("module.html", module=module_data, course=course, user=user)


@app.route('/unlock-module')
def unlock_module():
    user = current_user()
    if not user:
        flash("Login required to unlock modules.", "danger")
        return redirect(url_for('login'))
    return render_template("unlock_module.html", user=user)

# -------------------- Run App --------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
