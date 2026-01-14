import os
from flask import (
    Flask, jsonify, render_template, redirect, url_for,
    request, session, flash
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from datetime import datetime
# -------------------- Load Environment Variables --------------------
load_dotenv()

# -------------------- App Setup --------------------
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev_secret")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # simple path
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

# -------------------- Auth Routes -------------------

@app.route('/')
def index():
    return render_template('index.html', now=datetime.now())


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
@app.route('/dashboard')
def dashboard():
    user = current_user()
    if not user:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=user)

# -------------------- Courses & Modules --------------------
courses = { "Data Science": { "title": "Data Science", "icon": "📊", "description": "Learn how people use information to make better decisions.", "chapters": [
            {"id": 1,
                "title": "Introduction to Data Science",
                "description": "Understanding data science and why it matters",
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
                "free": True},
            {"id": 2,
                "title": "Data Types & Structures",
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
                "free": True},
            {"id": 3,
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
           {"id": 4,
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
    "free": True},
{"id": 5,
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
            {"id": 6,
    "title": "Feature Engineering Techniques",
    "description": "Transform raw data into useful features",
    "content": """
<div style="background-color:#0d1b22; color:#ffffff; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Feature Engineering</h4>
  <p>Feature engineering is about making raw information more useful. 
     Imagine you have a recipe book — the raw data is all the ingredients. 
     Feature engineering is like preparing those ingredients (chopping, mixing, seasoning) 
     so they’re ready to cook.</p>

  <h5 class="fw-bold mt-4">Simple Examples</h5>
  <ul>
    <li>Turning a date of birth into an age.</li>
    <li>Changing “Yes/No” answers into numbers (1 or 0).</li>
    <li>Combining two pieces of information, like height and weight, into one measure (BMI).</li>
  </ul>

  <p class="fst-italic mt-4">It’s like polishing raw materials so they can be used effectively in analysis or prediction.</p>
</div>
""",
    "free": False},
{"id": 7,
    "title": "Introduction to Machine Learning",
    "description": "Basic ML concepts and workflows",
    "content": """
<div style="background-color:#0d1b22; color:#ffffff; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Introduction to Machine Learning</h4>
  <p>Machine learning means teaching computers to learn from examples instead of giving them step‑by‑step instructions. 
     Think of it like training a child: you show them many pictures of cats and dogs, 
     and eventually they can tell the difference on their own.</p>

  <h5 class="fw-bold mt-4">How It Works</h5>
  <ul>
    <li><strong>Collect Examples:</strong> Gather data (like photos, numbers, or text).</li>
    <li><strong>Train the Computer:</strong> Show the computer patterns in the data.</li>
    <li><strong>Make Predictions:</strong> The computer uses what it learned to guess new answers.</li>
  </ul>

  <p class="fst-italic mt-4">In short, machine learning is about teaching computers to recognize patterns and make decisions, 
     just like people do when they gain experience.</p>
</div>
""",
    "free": False},
            {"id": 8,
    "title": "Supervised Learning: Regression Models",
    "description": "Linear and advanced regression",
    "content": """
<div style="background-color:#0d1b22; color:#ffffff; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Regression Models</h4>
  <p>Regression is about predicting numbers. Imagine you want to guess someone’s weight based on their height. 
     You look at many examples, draw a line through the points, and then use that line to make predictions.</p>

  <h5 class="fw-bold mt-4">Simple Examples</h5>
  <ul>
    <li>Predicting house prices from size and location.</li>
    <li>Estimating sales based on advertising spend.</li>
    <li>Guessing exam scores from hours studied.</li>
  </ul>

  <p class="fst-italic mt-4">Think of regression as drawing a best‑fit line through data to make educated guesses.</p>
</div>
""",
    "free": False},
{"id": 9,
    "title": "Supervised Learning: Classification Models",
    "description": "Logistic regression, decision trees",
    "content": """
<div style="background-color:#0d1b22; color:#ffffff; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Classification Models</h4>
  <p>Classification is about sorting things into groups. 
     Imagine you have a basket of fruits — you want the computer to learn how to separate apples from oranges. 
     You show it many examples, and it learns the differences.</p>

  <h5 class="fw-bold mt-4">Simple Examples</h5>
  <ul>
    <li>Deciding if an email is spam or not.</li>
    <li>Sorting medical images into “healthy” or “sick.”</li>
    <li>Recognizing handwritten digits (0–9).</li>
  </ul>

  <p class="fst-italic mt-4">Classification is like teaching a computer to play “spot the difference” and put items in the right box.</p>
</div>
""",
    "free": False},
            {"id": 10,
    "title": "Unsupervised Learning: Clustering",
    "description": "Grouping similar things together",
    "content": """
<div style="background-color:#0d1b22; color:#ffffff; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Clustering</h4>
  <p>Clustering is about finding groups in data without being told what the groups are. 
     Imagine you have a basket of mixed fruits — apples, bananas, and oranges — but no labels. 
     You look at their shapes and colors, and naturally sort them into groups.</p>

  <h5 class="fw-bold mt-4">Simple Examples</h5>
  <ul>
    <li>Grouping customers by shopping habits (without knowing categories beforehand).</li>
    <li>Sorting news articles into topics automatically.</li>
    <li>Organizing photos by similarity (faces, landscapes, animals).</li>
  </ul>

  <p class="fst-italic mt-4">Clustering is like letting the computer discover “hidden teams” inside your data.</p>
</div>
""",
    "free": False},
{"id": 11,
    "title": "Model Evaluation & Validation",
    "description": "Checking if predictions are reliable",
    "content": """
<div style="background-color:#0d1b22; color:#ffffff; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Model Evaluation & Validation</h4>
  <p>After teaching a computer to make predictions, we need to check if it’s doing a good job. 
     This is called evaluation and validation. It’s like testing a student after lessons to see if they really understood.</p>

  <h5 class="fw-bold mt-4">Simple Ways to Check</h5>
  <ul>
    <li>Split data into two sets: one for training, one for testing.</li>
    <li>See how often the computer’s answers match the real ones.</li>
    <li>Measure accuracy, errors, or how close predictions are to reality.</li>
  </ul>

  <p class="fst-italic mt-4">Evaluation is like giving your model an exam — it shows if it’s ready for real‑world use.</p>
</div>
""",
    "free": False},
            {"id": 12,
    "title": "Handling Big Data",
    "description": "Working with very large amounts of information",
    "content": """
<div style="background-color:#0d1b22; color:#ffffff; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Handling Big Data</h4>
  <p>Big Data simply means dealing with huge amounts of information — so much that it cannot fit neatly 
     into a small notebook or even a single computer. Imagine trying to count all the grains of sand on a beach. 
     You need special tools and smart ways to organize it.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <ul>
    <li><strong>Businesses:</strong> Track millions of customer purchases to see trends.</li>
    <li><strong>Healthcare:</strong> Study thousands of patient records to improve treatments.</li>
    <li><strong>Social Media:</strong> Analyze billions of posts to understand what people are talking about.</li>
  </ul>

  <h5 class="fw-bold mt-4">How We Handle It</h5>
  <ul>
    <li>Break the data into smaller pieces so it’s easier to manage.</li>
    <li>Use powerful computers that can work together as a team.</li>
    <li>Apply simple rules to quickly find patterns without reading every single detail.</li>
  </ul>

  <p class="fst-italic mt-4">Think of handling Big Data like organizing a giant library — 
     you don’t read every book, but you use systems to find the right one fast.</p>
</div>
""",
    "free": False},
           {"id": 13,
    "title": "Data Communication and Storytelling",
    "description": "Learn to present data effectively through visualizations and narratives.",
    "content": """
<div style="background-color:#0d1b22; color:#ffffff; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Data Communication and Storytelling</h4>
  <p>Data communication is about sharing information in a way people can easily understand. 
     Storytelling means turning numbers into a clear story that connects with your audience.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <ul>
    <li><strong>Clarity:</strong> People remember stories better than raw numbers.</li>
    <li><strong>Impact:</strong> A good chart or example can change how decisions are made.</li>
    <li><strong>Connection:</strong> Stories help audiences relate to the data personally.</li>
  </ul>

  <h5 class="fw-bold mt-4">Simple Examples</h5>
  <ul>
    <li>Instead of saying “Sales increased by 20%,” show a line chart that rises like a hill.</li>
    <li>Tell a short story: “Last year, 1 in 5 families struggled with internet access — here’s what that looks like.”</li>
    <li>Use visuals like bar charts or pie charts to make comparisons easy.</li>
  </ul>

  <p class="fst-italic mt-4">Think of data storytelling like being a tour guide: 
     you lead people through the numbers, highlight the important sights, 
     and explain why they matter.</p>
</div>
""",
    "free": False},
           {"id": 14,
    "title": "Deep Learning Foundations",
    "description": "Neural networks basics",
    "content": """
<div style="background-color:#0d1b22; color:#ffffff; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Deep Learning Foundations</h4>
  <p>Deep learning is a way of teaching computers to learn from lots of examples, 
     inspired by how our brains work. It uses “neural networks,” which are like 
     layers of decision‑makers stacked together.</p>

  <h5 class="fw-bold mt-4">Simple Analogy</h5>
  <p>Imagine a group of people passing notes: the first person looks at a picture 
     and guesses if it’s a cat or dog, then passes their guess to the next person, 
     who refines it, and so on. By the end, the group makes a strong decision together.</p>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li>Phones recognizing faces in photos.</li>
    <li>Voice assistants understanding speech.</li>
    <li>Apps translating languages automatically.</li>
  </ul>

  <p class="fst-italic mt-4">Deep learning is like building a team of tiny helpers, 
     each focusing on part of the problem, until the whole team solves it.</p>
</div>
""",
    "free": False},
{"id": 15,
    "title": "Capstone Project: End-to-End Workflow",
    "description": "Complete DS project",
    "content": """
<div style="background-color:#0d1b22; color:#ffffff; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Capstone Project: End-to-End Workflow</h4>
  <p>This final project brings everything together. You’ll go through the full 
     data science journey step by step, just like a real‑world project.</p>

  <h5 class="fw-bold mt-4">What You’ll Do</h5>
  <ul>
    <li><strong>Collect Data:</strong> Find or choose a dataset to work with.</li>
    <li><strong>Clean Data:</strong> Fix errors, remove duplicates, and make it tidy.</li>
    <li><strong>Explore:</strong> Summarize and visualize to see patterns.</li>
    <li><strong>Model:</strong> Try simple predictions or groupings.</li>
    <li><strong>Communicate:</strong> Share results with clear charts and a short story.</li>
  </ul>

  <p class="fst-italic mt-4">Think of the capstone as cooking a full meal: 
     you gather ingredients, prepare them, cook step by step, and finally serve 
     a dish that others can enjoy and understand.</p>
</div>
""",
    "free": False}
        ]},
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
        return redirect(url_for('course_detail', course_name=course_name))

    chapter_data = next((c for c in course["chapters"] if c["id"] == id), None)
    if not chapter_data:
        flash("Chapter not found.", "danger")
        return redirect(url_for('course_detail', course_name=course_name))

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
    return redirect(url_for('course_detail', course_name=course_name))

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
        return jsonify({"error": f"Order verification failed: {e}"}), 502

    # Step 3: Check status
    if order_data.get("status") == "COMPLETED":
        user.is_subscribed = True
        db.session.commit()
        flash("Payment verified. All courses unlocked! 🎉", "success")
        return jsonify({"status": "ok"})
    else:
        return jsonify({"error": "Payment not completed"}), 400

# -------------------- Run App --------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
