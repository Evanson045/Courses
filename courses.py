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
        "description": "Learn how people use information to make better decisions.",
        "modules": [
            {
                "id": 1,
                "title": "Introduction to Data Science",
                "description": "What data science is and why it matters",
                "content": """
<div style="background-color:#0d1b22; color:#ffffff; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">What Is Data Science?</h4>
  <p>Data science is about looking at information (like numbers, text, or pictures) and finding useful patterns. 
     It’s like being a detective, but instead of clues you use data.</p>

  <h5 class="fw-bold mt-4">Where It’s Used</h5>
  <ul>
    <li><strong>Shops:</strong> To know what customers like.</li>
    <li><strong>Hospitals:</strong> To predict illnesses and plan treatments.</li>
    <li><strong>Transport:</strong> To plan better routes and avoid delays.</li>
    <li><strong>Banks:</strong> To spot fraud and manage risks.</li>
  </ul>

  <p class="fst-italic mt-4">In short, data science helps us turn raw information into smart decisions.</p>
</div>
""",
                "free": True
            },
            {
                "id": 2,
                "title": "Understanding Data Types & Structures",
                "description": "Different kinds of information and how we organize them",
                "content": """
<div style="background-color:#0d1b22; color:#ffffff; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Data Types & Structures</h4>
  <p>Think of data types as the “kind” of information: numbers, words, or yes/no answers. 
     Data structures are just ways to keep this information organized, like lists or tables.</p>

  <h5 class="fw-bold mt-4">Examples</h5>
  <ul>
    <li><strong>Numbers:</strong> Age, height, or prices.</li>
    <li><strong>Words:</strong> Names or places.</li>
    <li><strong>Yes/No:</strong> Is the student enrolled? True or False.</li>
  </ul>

  <p><strong>Organizing Data:</strong> A shopping list is a simple data structure. Each item is a piece of data. 
     A table of students with names and ages is another structure.</p>

  <p class="fst-italic mt-4">Organizing data properly makes it easier to understand and use.</p>
</div>
""",
                "free": True
            },
            {
                "id": 3,
                "title": "Data Cleaning Basics",
                "description": "Making messy information neat and usable",
                "content": """
<div style="background-color:#0d1b22; color:#ffffff; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Data Cleaning Basics</h4>
  <p>Sometimes information is messy — like spelling mistakes, missing answers, or repeated entries. 
     Data cleaning is just tidying it up so it makes sense.</p>

  <h5 class="fw-bold mt-4">Key Steps</h5>
  <ul>
    <li><strong>Remove Duplicates:</strong> If the same person is listed twice, keep only one.</li>
    <li><strong>Fill Missing Values:</strong> If someone forgot to write their age, we can estimate or leave it blank clearly.</li>
    <li><strong>Fix Errors:</strong> Correct typos or wrong formats (like “Nrb” → “Nairobi”).</li>
    <li><strong>Standardize:</strong> Make dates, names, and categories consistent.</li>
  </ul>

  <p class="fst-italic mt-4">Clean data is like a tidy room — easier to work in and more reliable.</p>
</div>
""",
                "free": True},
           {
    "id": 4,
    "title": "Exploratory Data Analysis (EDA)",
    "description": "Summarize and visualize datasets",
    "content": """
<div style="background-color:#0d1b22; color:#ffffff; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Exploratory Data Analysis (EDA)</h4>
  <p>EDA is like taking a first look at your information to see what’s inside. 
     Imagine you open a box of survey answers — before doing anything complicated, 
     you count, sort, and make simple charts to understand the basics.</p>

  <h5 class="fw-bold mt-4">What You Do in EDA</h5>
  <ul>
    <li>Check how many records you have.</li>
    <li>Look for missing or unusual values.</li>
    <li>Make simple graphs to see trends.</li>
    <li>Ask: “What story is this data telling me?”</li>
  </ul>

  <p class="fst-italic mt-4">Think of EDA as the “getting to know you” stage with your data.</p>
</div>
""",
    "free": True
},
{
    "id": 5,
    "title": "Data Visualization Techniques",
    "description": "Create charts and plots",
    "content": """
<div style="background-color:#0d1b22; color:#ffffff; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Data Visualization</h4>
  <p>Data visualization means turning numbers into pictures. 
     Instead of staring at a long list of values, you make a chart or graph 
     so patterns jump out clearly.</p>

  <h5 class="fw-bold mt-4">Common Visuals</h5>
  <ul>
    <li><strong>Bar Chart:</strong> Compare categories (like sales in different shops).</li>
    <li><strong>Line Graph:</strong> Show change over time (like daily temperatures).</li>
    <li><strong>Pie Chart:</strong> Show parts of a whole (like budget spending).</li>
  </ul>

  <p class="fst-italic mt-4">It’s like telling a story with pictures instead of words — 
     easier to understand at a glance.</p>
</div>
""",
    "free": True},
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
            {"id": 8, "title": "Correlation & Regression Analysis", "description": "Relationships between variables",
             "content": "Explore correlation coefficients to measure relationships between variables. Learn simple and multiple regression analysis to model and predict outcomes.",
             "free": False},
            {"id": 9, "title": "ANOVA & Comparing Groups", "description": "Analysis of variance",
             "content": "Understand how to compare means across multiple groups using ANOVA. Learn assumptions, F-tests, and post-hoc comparisons.",
             "free": False},
            {"id": 10, "title": "Nonparametric Methods", "description": "Tests without distribution assumptions",
             "content": "Learn statistical tests that do not rely on normal distribution assumptions, such as the Mann-Whitney U test and Kruskal-Wallis test.",
             "free": False},
            {"id": 11, "title": "Bayesian Statistics Introduction", "description": "Bayes theorem and applications",
             "content": "Understand Bayes’ theorem and its applications in updating probabilities. Learn the basics of Bayesian inference and prior/posterior distributions.",
             "free": False},
            {"id": 12, "title": "Multivariate Statistics", "description": "Multiple variables analysis",
             "content": "Explore techniques for analyzing datasets with multiple variables, including principal component analysis (PCA) and factor analysis.",
             "free": False},
            {"id": 13, "title": "Time Series Analysis", "description": "Forecasting and trends",
             "content": "Learn methods for analyzing data collected over time. Explore moving averages, ARIMA models, and trend forecasting.",
             "free": False},
            {"id": 14, "title": "Statistical Modeling in Practice", "description": "Applied modeling techniques",
             "content": "Apply statistical models to real-world problems. Learn model selection, diagnostics, and interpretation of results in practical contexts.",
             "free": False},
            {"id": 15, "title": "Capstone Project: Statistical Report", "description": "Complete statistical analysis project",
             "content": "Conduct a full statistical analysis project from data collection to reporting. Apply descriptive statistics, inference, regression, and present findings in a professional report.",
             "free": False},
        ]
    },
"R Programming": {
    "title": "R Programming",
    "icon": "💻",
    "description": "Build reproducible workflows and powerful analytics with R.",
    "modules": [
        {"id": 1, "title": "Introduction to R & RStudio", "description": "Getting started with R environment",
         "content": "Install R and RStudio, learn basic syntax, and write your first R scripts. Explore the R console, script editor, and workspace management.",
         "free": True},
        {"id": 2, "title": "Data Types & Structures in R", "description": "Vectors, lists, data frames",
         "content": "Understand vectors, lists, matrices, and data frames — the building blocks of R programming. Learn how to manipulate and access elements efficiently.",
         "free": True},
        {"id": 3, "title": "Importing & Cleaning Data in R", "description": "Read and clean datasets",
         "content": "Learn how to import CSV, Excel, and text files into R. Practice cleaning datasets by handling missing values, duplicates, and inconsistent formats.",
         "free": True},
        {"id": 4, "title": "Data Manipulation with dplyr", "description": "Filter, group, summarize data",
         "content": "Use dplyr functions such as filter, select, mutate, group_by, and summarize to transform and analyze datasets efficiently.",
         "free": True},
        {"id": 5, "title": "Data Visualization with ggplot2", "description": "Create plots and charts",
         "content": "Create bar charts, scatter plots, line graphs, and histograms using ggplot2. Learn aesthetics, layers, and themes for professional visualizations.",
         "free": True},
        {"id": 6, "title": "Writing Functions & Modular Code", "description": "Reusable R functions",
         "content": "Learn how to write custom functions in R to automate tasks. Explore modular coding practices for reproducibility and clarity.",
         "free": False},
        {"id": 7, "title": "Control Structures & Iteration", "description": "Loops and conditionals",
         "content": "Understand control structures such as if/else statements, for loops, and while loops. Apply iteration to automate repetitive tasks.",
         "free": False},
        {"id": 8, "title": "Statistical Analysis in R", "description": "Basic statistical tests",
         "content": "Perform t-tests, chi-square tests, and correlation analysis in R. Learn how to interpret statistical outputs and apply them to real datasets.",
         "free": False},
        {"id": 9, "title": "Working with Dates & Strings", "description": "Handle date-time and text data",
         "content": "Use R packages like lubridate and stringr to manipulate dates and text. Learn parsing, formatting, and cleaning techniques.",
         "free": False},
        {"id": 10, "title": "Data Reshaping with tidyr", "description": "Tidy data principles",
         "content": "Apply tidyr functions such as pivot_longer, pivot_wider, and separate to reshape datasets into tidy formats for analysis.",
         "free": False},
        {"id": 11, "title": "Advanced Visualization Techniques", "description": "Interactive plots",
         "content": "Explore advanced visualization libraries like plotly and highcharter. Create interactive plots and dashboards for deeper insights.",
         "free": False},
        {"id": 12, "title": "Introduction to Shiny Apps", "description": "Build web apps with R",
         "content": "Learn how to build interactive web applications using Shiny. Create UI components and server logic to share analyses online.",
         "free": False},
        {"id": 13, "title": "R Markdown for Reporting", "description": "Dynamic documents",
         "content": "Use R Markdown to create dynamic reports that integrate code, outputs, and narrative text. Export reports to HTML, PDF, or Word.",
         "free": False},
        {"id": 14, "title": "Package Development Basics", "description": "Create R packages",
         "content": "Learn the structure of an R package, how to document functions, and share reusable code with others.",
         "free": False},
        {"id": 15, "title": "Capstone Project: R Analysis", "description": "Complete data analysis project in R",
         "content": "Apply all learned skills to a real dataset. Perform cleaning, manipulation, visualization, statistical analysis, and present results in a final report.",
         "free": False},
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

@app.route('/courses/<course_name>/module/<int:id>')
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

    return render_template("module.html", module=module_data, course=course, user=user, course_name=course_name)

@app.route('/unlock-module')
def unlock_module():
    user = current_user()
    if not user:
        flash("Login required to unlock modules.", "danger")
        return redirect(url_for('login'))
    return render_template("unlock_module.html", user=user)

@app.route('/unlock-all')
def unlock_all():
    user = current_user()
    if not user:
        flash("Login required to unlock modules.", "danger")
        return redirect(url_for('login'))

    if not user.is_subscribed:
        user.is_subscribed = True
        db.session.commit()
        flash("All modules unlocked successfully! 🎉", "success")

    return redirect(url_for('dashboard'))


# -------------------- Run App --------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
