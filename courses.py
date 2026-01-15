# -------------------- Courses & Modules --------------------
courses = {"Data Science": {"title": "Data Science", "icon": "📊", "description": "Learn how people use information to make better decisions.", "chapters":
                            [
            {"id": 1,
 "title": "Introduction to Data Science",
 "description": "Understanding data science and why it matters",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">What Is Data Science?</h4>
  <p>Data science is the practice of collecting, organizing, and studying information to find useful patterns. 
     It’s like being a detective, but instead of clues you use data such as numbers, words, or pictures. 
     The goal is to turn raw information into insights that help people make better decisions.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Every day, huge amounts of data are created — from online shopping, hospital records, 
     traffic sensors, and even social media posts. Without data science, this information 
     would just sit unused. With data science, we can discover trends, predict outcomes, 
     and solve real problems in smarter ways.</p>

  <h5 class="fw-bold mt-4">Where It’s Used</h5>
  <ul>
    <li><strong>Shops:</strong> To understand what customers like and recommend products they may buy.</li>
    <li><strong>Hospitals:</strong> To predict illnesses, plan treatments, and improve patient care.</li>
    <li><strong>Transport:</strong> To design better routes, reduce delays, and save fuel.</li>
    <li><strong>Banks:</strong> To detect fraud, manage risks, and keep money safe.</li>
    <li><strong>Social Media:</strong> To analyze posts and see what topics people are talking about.</li>
  </ul>

  <h5 class="fw-bold mt-4">Simple Example</h5>
  <p>Imagine a school collecting exam scores. By looking at the data, teachers can see 
     which subjects students struggle with and provide extra help. That’s data science 
     in action — using information to guide better decisions.</p>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Data science is not just about numbers. It’s about asking questions like: 
     “What story does this data tell?” and “How can we use this story to improve lives?”</p>

  <p class="fst-italic mt-4">In short, data science helps us turn raw information into smart, practical decisions 
     that make everyday life easier and more efficient.</p>
</div>
""", "free": True},
            {"id": 2,
 "title": "Data Types & Structures",
 "description": "Different kinds of information and how we organize them",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Data Types & Structures</h4>
  <p>Data comes in different forms. A <strong>data type</strong> tells us what kind of information we are dealing with — 
     whether it’s a number, a word, or a simple yes/no answer. A <strong>data structure</strong> is how we arrange 
     that information so it’s easy to use, like putting items neatly in boxes or rows.</p>

  <h5 class="fw-bold mt-4">Common Data Types</h5>
  <ul>
    <li><strong>Numbers:</strong> Things we can count or measure, like age, height, or prices.</li>
    <li><strong>Words (Text):</strong> Names, places, or descriptions written in letters.</li>
    <li><strong>Yes/No (Boolean):</strong> Simple answers like True/False or On/Off.</li>
    <li><strong>Dates & Times:</strong> Information about when something happened, like birthdays or schedules.</li>
  </ul>

  <h5 class="fw-bold mt-4">Simple Data Structures</h5>
  <ul>
    <li><strong>Lists:</strong> A shopping list is a data structure. Each item is a piece of data.</li>
    <li><strong>Tables:</strong> A class register with names and ages is a table structure.</li>
    <li><strong>Pairs:</strong> A phone book matches names with numbers — that’s a structure too.</li>
    <li><strong>Groups:</strong> Organizing students by grade level is another way to structure data.</li>
  </ul>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Organizing data properly makes it easier to understand and use. Imagine trying to find a book in a library 
     without shelves or categories — it would be chaos. Data structures give us “shelves” and “labels” so we can 
     quickly find what we need.</p>

  <h5 class="fw-bold mt-4">Everyday Example</h5>
  <p>Think about your phone contacts. Each contact has a name (text), a phone number (number), and maybe a birthday (date). 
     Together, they form a structured list that makes calling or messaging easy.</p>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Data types tell us <em>what</em> the information is. Data structures tell us <em>how</em> it’s arranged. 
     When combined, they make raw information clear, useful, and ready for analysis.</p>

  <p class="fst-italic mt-4">In short, data types are the building blocks, and data structures are the way we stack them neatly.</p>
</div>
""",
 "free": True},
            {"id": 3,
 "title": "Data Cleaning Basics",
 "description": "Making messy information neat and usable",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Data Cleaning Basics</h4>
  <p>Data is rarely perfect when we first collect it. Sometimes there are spelling mistakes, missing answers, 
     repeated entries, or values written in different formats. <strong>Data cleaning</strong> is the process of 
     tidying up this information so it makes sense and can be trusted.</p>

  <h5 class="fw-bold mt-4">Why Cleaning Matters</h5>
  <p>Imagine trying to cook in a messy kitchen — ingredients scattered everywhere, labels missing, and duplicates 
     of the same spice. It would be confusing and slow. Clean data is like a tidy kitchen: everything is in order, 
     easy to find, and ready to use.</p>

  <h5 class="fw-bold mt-4">Key Steps</h5>
  <ul>
    <li><strong>Remove Duplicates:</strong> If the same person or record appears twice, keep only one copy.</li>
    <li><strong>Fill Missing Values:</strong> If someone forgot to write their age, we can estimate, leave it blank clearly, or mark it as “unknown.”</li>
    <li><strong>Fix Errors:</strong> Correct typos or wrong formats (like “Nrb” → “Nairobi”).</li>
    <li><strong>Standardize:</strong> Make dates, names, and categories consistent (e.g., “Jan 1, 2025” vs “01/01/25”).</li>
    <li><strong>Remove Outliers:</strong> Spot values that don’t make sense, like a height of 500 cm, and check if they are mistakes.</li>
    <li><strong>Check Consistency:</strong> Ensure related data matches — for example, if someone’s birth year is 2010, their age should be around 15, not 50.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Example</h5>
  <p>Think about a school attendance list. If a student’s name is spelled differently each time (“Ann” vs “Anne”), 
     or if their age is missing, the list becomes confusing. Cleaning the data means fixing the spelling, filling 
     the missing age, and making sure each student appears only once.</p>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Clean data is reliable data. It saves time, reduces mistakes, and makes analysis more accurate. 
     Without cleaning, even the best tools or models will give poor results because they are working with 
     messy information.</p>

  <p class="fst-italic mt-4">In short, clean data is like a tidy room — easier to work in, more comfortable, 
     and far more useful.</p>
</div>
""",
 "free": True},
          {"id": 4,
 "title": "Exploratory Data Analysis (EDA)",
 "description": "Summarize and visualize datasets",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Exploratory Data Analysis (EDA)</h4>
  <p>Exploratory Data Analysis (EDA) is the process of taking a first look at your information 
     to understand what’s inside. Before building models or making predictions, you need to 
     explore the data — just like opening a box of survey answers and checking what people wrote 
     before doing anything complicated.</p>

  <h5 class="fw-bold mt-4">Why EDA Matters</h5>
  <p>EDA helps you spot problems early and discover useful patterns. Without it, you might miss 
     important details or build models on messy data. Think of EDA as the “getting to know you” 
     stage with your dataset — you ask simple questions and let the data tell its story.</p>

  <h5 class="fw-bold mt-4">What You Do in EDA</h5>
  <ul>
    <li><strong>Count Records:</strong> See how many rows or entries you have.</li>
    <li><strong>Check Missing Values:</strong> Find gaps where information is missing.</li>
    <li><strong>Spot Unusual Values:</strong> Look for numbers that don’t make sense, like a negative age.</li>
    <li><strong>Summarize:</strong> Calculate averages, minimums, maximums, and totals.</li>
    <li><strong>Visualize:</strong> Make simple graphs like bar charts or line plots to see trends.</li>
    <li><strong>Compare Groups:</strong> Break data into categories (like male vs female, or region A vs region B) to see differences.</li>
    <li><strong>Ask Questions:</strong> “What story is this data telling me?” or “What patterns stand out?”</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Example</h5>
  <p>Imagine a shop owner looking at sales data. By exploring the data, they notice that 
     sales are higher on weekends, certain products sell more in December, and some items 
     rarely sell at all. This simple exploration helps them plan better promotions and stock 
     the right products.</p>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>EDA is not about complex math. It’s about curiosity — asking basic questions, 
     making simple charts, and letting the data guide your next steps. Once you understand 
     the shape and story of your data, you can move confidently into deeper analysis.</p>

  <p class="fst-italic mt-4">In short, EDA is like meeting your data for the first time — 
     you listen, observe, and learn before making big decisions.</p>
</div>
""",
 "free": True},
{"id": 5,
 "title": "Data Visualization Techniques",
 "description": "Create charts and plots",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Data Visualization</h4>
  <p>Data visualization means turning numbers into pictures. Instead of staring at a long list of values, 
     you make a chart or graph so patterns jump out clearly. A good visualization helps people understand 
     information quickly and spot trends that might be hidden in raw numbers.</p>

  <h5 class="fw-bold mt-4">Why Visualization Matters</h5>
  <p>Humans understand visuals faster than text or tables. A chart can show in seconds what might take 
     minutes to read in a spreadsheet. Visualization makes data more engaging, easier to share, and 
     more persuasive when presenting ideas.</p>

  <h5 class="fw-bold mt-4">Common Visuals</h5>
  <ul>
    <li><strong>Bar Chart:</strong> Compare categories, like sales in different shops.</li>
    <li><strong>Line Graph:</strong> Show change over time, like daily temperatures or monthly revenue.</li>
    <li><strong>Pie Chart:</strong> Show parts of a whole, like budget spending or market share.</li>
    <li><strong>Histogram:</strong> Show how often values appear, like exam score distributions.</li>
    <li><strong>Scatter Plot:</strong> Show relationships between two variables, like height vs. weight.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Example</h5>
  <p>Imagine a teacher looking at student grades. A table of scores is hard to scan, but a bar chart 
     instantly shows which subjects students perform best in. Or think of a family budget: a pie chart 
     makes it clear how much money goes to food, rent, or entertainment.</p>

  <h5 class="fw-bold mt-4">Tips for Good Visuals</h5>
  <ul>
    <li>Keep charts simple — avoid too many colors or labels.</li>
    <li>Choose the right chart for the data (don’t use a pie chart for time trends).</li>
    <li>Label clearly so viewers know what they’re looking at.</li>
    <li>Use consistent scales to avoid misleading impressions.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Visualization is not just decoration. It’s a way of telling a story with data. 
     The right chart can highlight problems, reveal opportunities, and make decisions easier.</p>

  <p class="fst-italic mt-4">In short, data visualization is like turning a book of numbers into a picture book — 
     faster to read, easier to enjoy, and more memorable.</p>
</div>
""",
 "free": True},
            {"id": 6,
 "title": "Feature Engineering Techniques",
 "description": "Transform raw data into useful features",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Feature Engineering</h4>
  <p>Feature engineering is the process of transforming raw information into forms that are more useful for analysis or prediction. 
     Imagine you have a recipe book — the raw data is all the ingredients. Feature engineering is like preparing those ingredients 
     (washing, chopping, mixing, seasoning) so they’re ready to cook a proper meal. Without this preparation, the recipe won’t work well.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Most datasets don’t come ready for analysis. They need to be reshaped into meaningful features that capture the essence of the problem. 
     Good features make models smarter and results more accurate. Poor features can confuse models and lead to weak predictions.</p>

  <h5 class="fw-bold mt-4">Simple Examples</h5>
  <ul>
    <li><strong>Dates:</strong> Turning a date of birth into an age, or extracting the month from a timestamp to see seasonal trends.</li>
    <li><strong>Yes/No Answers:</strong> Changing “Yes/No” responses into numbers (1 or 0) so computers can process them.</li>
    <li><strong>Combining Data:</strong> Using height and weight together to calculate Body Mass Index (BMI).</li>
    <li><strong>Categories:</strong> Converting text categories (like “Red,” “Blue,” “Green”) into numeric codes or dummy variables.</li>
    <li><strong>Text:</strong> Counting words in a sentence or checking if certain keywords appear in a review.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Example</h5>
  <p>Think about an online store. Raw data might include the date and time of each purchase. By engineering features, 
     we can create new information like “day of the week,” “holiday vs. non-holiday,” or “time of day.” These features 
     help the store predict when customers are most likely to shop.</p>

  <h5 class="fw-bold mt-4">Tips for Good Feature Engineering</h5>
  <ul>
    <li>Keep features simple and meaningful — don’t add complexity without purpose.</li>
    <li>Use domain knowledge — think about what matters in the real world.</li>
    <li>Test new features — check if they actually improve predictions.</li>
    <li>Avoid redundancy — don’t create features that repeat the same information.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Feature engineering is about polishing raw materials so they can be used effectively in analysis or prediction. 
     It bridges the gap between messy real-world data and the clean, structured inputs that models need to perform well.</p>

  <p class="fst-italic mt-4">In short, feature engineering is like preparing ingredients before cooking — 
     the better the preparation, the better the final dish.</p>
</div>
""",
 "free": False},
{"id": 7,
 "title": "Introduction to Machine Learning",
 "description": "Basic ML concepts and workflows",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Introduction to Machine Learning</h4>
  <p>Machine learning is about teaching computers to learn from examples instead of giving them step‑by‑step instructions. 
     Think of it like training a child: you show them many pictures of cats and dogs, and eventually they can tell the difference on their own. 
     The computer doesn’t memorize every picture — it learns patterns that help it make decisions.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Machine learning powers many tools we use every day. It helps email apps filter spam, streaming services recommend movies, 
     and doctors predict illnesses. Without machine learning, computers would only follow fixed rules and struggle with complex, changing problems.</p>

  <h5 class="fw-bold mt-4">How It Works</h5>
  <ul>
    <li><strong>Collect Examples:</strong> Gather data such as photos, numbers, or text. The more examples, the better the computer can learn.</li>
    <li><strong>Train the Computer:</strong> Feed the data into algorithms that look for patterns. This is like practice sessions for the computer.</li>
    <li><strong>Test the Learning:</strong> Check how well the computer performs on new, unseen data.</li>
    <li><strong>Make Predictions:</strong> Once trained, the computer uses what it learned to guess new answers or classify new items.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Email:</strong> Sorting messages into “Inbox” or “Spam.”</li>
    <li><strong>Shopping:</strong> Recommending products based on what you bought before.</li>
    <li><strong>Transport:</strong> Predicting traffic jams and suggesting faster routes.</li>
    <li><strong>Healthcare:</strong> Spotting early signs of disease from medical records.</li>
  </ul>

  <h5 class="fw-bold mt-4">Types of Machine Learning</h5>
  <ul>
    <li><strong>Supervised Learning:</strong> The computer learns from labeled examples (like photos marked “cat” or “dog”).</li>
    <li><strong>Unsupervised Learning:</strong> The computer groups data without labels, finding hidden patterns (like clustering customers by shopping habits).</li>
    <li><strong>Reinforcement Learning:</strong> The computer learns by trial and error, like a game player improving with practice.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Machine learning is about recognizing patterns and making decisions, just like people do when they gain experience. 
     The more examples the computer sees, the smarter it becomes. It’s not magic — it’s practice, repetition, and learning from data.</p>

  <p class="fst-italic mt-4">In short, machine learning helps computers move beyond fixed rules, 
     giving them the ability to adapt, improve, and make smarter choices over time.</p>
</div>
""",
 "free": False},
            {"id": 8,
 "title": "Supervised Learning: Regression Models",
 "description": "Linear and advanced regression",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Regression Models</h4>
  <p>Regression is about predicting numbers. It helps us estimate values based on patterns in data. 
     Imagine you want to guess someone’s weight based on their height. You look at many examples, 
     draw a line through the points, and then use that line to make predictions. 
     This line is called a <strong>regression line</strong>, and it represents the best fit for the data.</p>

  <h5 class="fw-bold mt-4">Why Regression Matters</h5>
  <p>Regression is one of the most common tools in data science. It allows us to forecast future values, 
     measure relationships between variables, and make informed decisions. Businesses, schools, and 
     governments all use regression to plan ahead and understand trends.</p>

  <h5 class="fw-bold mt-4">Simple Examples</h5>
  <ul>
    <li><strong>Housing:</strong> Predicting house prices from size, location, and number of bedrooms.</li>
    <li><strong>Sales:</strong> Estimating sales based on advertising spend or number of customers.</li>
    <li><strong>Education:</strong> Guessing exam scores from hours studied or attendance rates.</li>
    <li><strong>Health:</strong> Predicting blood pressure based on age and lifestyle factors.</li>
  </ul>

  <h5 class="fw-bold mt-4">Types of Regression</h5>
  <ul>
    <li><strong>Linear Regression:</strong> Draws a straight line through the data to make predictions.</li>
    <li><strong>Multiple Regression:</strong> Uses more than one factor (like size and location together) to predict outcomes.</li>
    <li><strong>Polynomial Regression:</strong> Fits curves instead of straight lines when data has more complex patterns.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Example</h5>
  <p>Imagine a farmer tracking rainfall and crop yield. By using regression, they can see how rainfall 
     affects harvest size. With this knowledge, they can predict future yields and plan resources better.</p>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Regression is about finding the relationship between variables and using it to make educated guesses. 
     It doesn’t give perfect answers, but it provides useful estimates that guide decisions. 
     The more data you have, the more reliable your regression model becomes.</p>

  <p class="fst-italic mt-4">In short, regression is like drawing a best‑fit line through data to make smart predictions 
     about the future.</p>
</div>
""",
 "free": False},
{"id": 9,
 "title": "Supervised Learning: Classification Models",
 "description": "Logistic regression, decision trees",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Classification Models</h4>
  <p>Classification is about sorting things into groups. Instead of predicting a number, 
     the goal is to decide which category something belongs to. Imagine you have a basket of fruits — 
     you want the computer to learn how to separate apples from oranges. You show it many examples, 
     and it learns the differences so it can classify new fruits correctly.</p>

  <h5 class="fw-bold mt-4">Why Classification Matters</h5>
  <p>Classification is used everywhere. It helps email systems filter spam, doctors identify diseases, 
     and banks detect fraud. By teaching computers to recognize categories, we can automate decisions 
     that would otherwise take a lot of human effort.</p>

  <h5 class="fw-bold mt-4">Simple Examples</h5>
  <ul>
    <li><strong>Email:</strong> Deciding if a message is spam or not.</li>
    <li><strong>Healthcare:</strong> Sorting medical images into “healthy” or “sick.”</li>
    <li><strong>Education:</strong> Recognizing handwritten digits (0–9) for exam grading.</li>
    <li><strong>Finance:</strong> Flagging transactions as “normal” or “suspicious.”</li>
    <li><strong>Retail:</strong> Predicting if a customer will buy a product or not.</li>
  </ul>

  <h5 class="fw-bold mt-4">Common Classification Models</h5>
  <ul>
    <li><strong>Logistic Regression:</strong> A simple model that predicts categories using probabilities.</li>
    <li><strong>Decision Trees:</strong> Models that split data into branches based on rules (like “Is age > 18?”).</li>
    <li><strong>Random Forests:</strong> A collection of decision trees working together for stronger predictions.</li>
    <li><strong>Support Vector Machines:</strong> Models that find the best boundary between categories.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Example</h5>
  <p>Imagine a bank trying to detect fraud. By training a classification model on past transactions, 
     the computer learns patterns of normal spending versus suspicious activity. When a new transaction 
     comes in, the model quickly decides whether to approve it or flag it for review.</p>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Classification is like teaching a computer to play “spot the difference” and put items in the right box. 
     It doesn’t give exact numbers, but it helps us make clear yes/no or category decisions. 
     The more examples the computer sees, the better it becomes at sorting new data correctly.</p>

  <p class="fst-italic mt-4">In short, classification helps computers recognize categories, 
     making everyday tasks faster, safer, and more reliable.</p>
</div>
""",
 "free": False},
            {"id": 10,
 "title": "Unsupervised Learning: Clustering",
 "description": "Grouping similar things together",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Clustering</h4>
  <p>Clustering is about finding groups in data without being told what the groups are. 
     Unlike supervised learning, where we train with labeled examples, clustering lets 
     the computer discover patterns on its own. Imagine you have a basket of mixed fruits — 
     apples, bananas, and oranges — but no labels. You look at their shapes and colors, 
     and naturally sort them into groups. That’s clustering.</p>

  <h5 class="fw-bold mt-4">Why Clustering Matters</h5>
  <p>Clustering helps us uncover hidden structures in data. It’s useful when we don’t 
     know the categories beforehand. Businesses use it to understand customers, 
     scientists use it to group species, and apps use it to organize photos. 
     It’s a way of letting the data speak for itself.</p>

  <h5 class="fw-bold mt-4">Simple Examples</h5>
  <ul>
    <li><strong>Shopping:</strong> Grouping customers by shopping habits (without knowing categories beforehand).</li>
    <li><strong>News:</strong> Sorting articles into topics automatically, like sports, politics, or entertainment.</li>
    <li><strong>Photos:</strong> Organizing images by similarity (faces, landscapes, animals).</li>
    <li><strong>Healthcare:</strong> Grouping patients with similar symptoms to discover new patterns in diseases.</li>
    <li><strong>Education:</strong> Clustering students by learning styles or performance levels.</li>
  </ul>

  <h5 class="fw-bold mt-4">Common Clustering Methods</h5>
  <ul>
    <li><strong>K-Means:</strong> Splits data into a chosen number of groups by finding cluster centers.</li>
    <li><strong>Hierarchical Clustering:</strong> Builds a tree of groups, starting small and merging into bigger clusters.</li>
    <li><strong>DBSCAN:</strong> Finds clusters based on density, useful for irregular shapes or noisy data.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Example</h5>
  <p>Imagine a music app analyzing listening habits. Without knowing genres, it notices 
     that some users listen mostly to jazz, others to pop, and others to classical. 
     By clustering users into these groups, the app can recommend songs more effectively.</p>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Clustering is like letting the computer discover “hidden teams” inside your data. 
     It doesn’t need labels — it just looks for similarities and groups things together. 
     This makes clustering powerful for exploration, pattern discovery, and organizing 
     large amounts of information.</p>

  <p class="fst-italic mt-4">In short, clustering is about uncovering natural groups in data, 
     helping us see structure where none was obvious before.</p>
</div>
""",
 "free": False},
{"id": 11,
 "title": "Model Evaluation & Validation",
 "description": "Checking if predictions are reliable",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Model Evaluation & Validation</h4>
  <p>After teaching a computer to make predictions, we need to check if it’s doing a good job. 
     This process is called <strong>evaluation</strong> and <strong>validation</strong>. 
     It’s like testing a student after lessons to see if they really understood the material. 
     Without evaluation, we can’t be sure if the model is reliable or ready for real‑world use.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Models can look smart during training but fail when faced with new data. 
     Evaluation ensures that the computer isn’t just memorizing examples but actually learning patterns. 
     Validation helps us confirm that predictions will hold up outside the classroom — in real life. 
     Without these checks, even advanced models can give misleading results.</p>

  <h5 class="fw-bold mt-4">Simple Ways to Check</h5>
  <ul>
    <li><strong>Train/Test Split:</strong> Divide data into two sets — one for training, one for testing — to see how well the model performs on unseen data.</li>
    <li><strong>Accuracy:</strong> Measure how often the computer’s answers match the real ones.</li>
    <li><strong>Error Rates:</strong> Look at how far predictions are from actual values (like predicting 80 when the real answer is 85).</li>
    <li><strong>Confusion Matrix:</strong> For classification, check how often the model gets each category right or wrong.</li>
    <li><strong>Cross‑Validation:</strong> Test the model on different slices of the data to make sure results are consistent.</li>
    <li><strong>Precision & Recall:</strong> For tasks like medical diagnosis, check how often the model correctly identifies positives and negatives.</li>
    <li><strong>F1 Score:</strong> Combine precision and recall into one balanced measure.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Example</h5>
  <p>Imagine a doctor’s diagnostic tool trained to spot illnesses. 
     If it only works on the training data but fails on new patients, it’s not useful. 
     By evaluating with test data, doctors can see if the tool is truly reliable before using it in practice. 
     Similarly, a bank’s fraud detection system must be tested on new transactions to ensure it catches fraud 
     without blocking normal purchases.</p>

  <h5 class="fw-bold mt-4">Tips for Good Evaluation</h5>
  <ul>
    <li>Always test with data the model hasn’t seen before.</li>
    <li>Use multiple metrics — accuracy alone doesn’t tell the full story.</li>
    <li>Watch out for <strong>overfitting</strong> (when a model memorizes instead of learning).</li>
    <li>Compare different models to choose the best one for the task.</li>
    <li>Keep evaluation simple and clear so non‑technical audiences can understand results.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Evaluation and validation are like exams for your model. 
     They show whether the computer has truly learned or is just guessing. 
     A well‑evaluated model gives confidence that predictions are trustworthy and ready for real‑world use. 
     Without evaluation, models may look impressive but fail when it matters most.</p>

  <p class="fst-italic mt-4">In short, evaluation is the final check — the step that proves your model is ready to perform outside the classroom and deliver reliable results.</p>
</div>
""",
 "free": False},
           {"id": 12,
 "title": "Handling Big Data",
 "description": "Working with very large amounts of information",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Handling Big Data</h4>
  <p><strong>Big Data</strong> simply means dealing with huge amounts of information — so much that it cannot fit neatly 
     into a small notebook or even a single computer. Imagine trying to count all the grains of sand on a beach. 
     You would need special tools and smart ways to organize it. That’s what Big Data is about: finding ways to 
     manage, store, and analyze information at a massive scale.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Big Data is everywhere. Every time you shop online, post on social media, or visit a hospital, 
     new data is created. Companies and organizations use this information to make better decisions, 
     improve services, and discover new opportunities.</p>
  <ul>
    <li><strong>Businesses:</strong> Track millions of customer purchases to see trends and predict demand.</li>
    <li><strong>Healthcare:</strong> Study thousands of patient records to improve treatments and spot risks early.</li>
    <li><strong>Social Media:</strong> Analyze billions of posts to understand what people are talking about worldwide.</li>
    <li><strong>Transport:</strong> Use traffic sensors and GPS data to plan routes and reduce congestion.</li>
    <li><strong>Education:</strong> Review student performance data to personalize learning and improve outcomes.</li>
  </ul>

  <h5 class="fw-bold mt-4">How We Handle It</h5>
  <p>Because Big Data is too large for one computer to handle, we use special techniques and tools:</p>
  <ul>
    <li><strong>Divide and Conquer:</strong> Break the data into smaller pieces so it’s easier to manage.</li>
    <li><strong>Distributed Systems:</strong> Use powerful computers that can work together as a team (like Hadoop or Spark).</li>
    <li><strong>Cloud Storage:</strong> Store data online where it can grow as needed without running out of space.</li>
    <li><strong>Quick Rules:</strong> Apply simple algorithms to find patterns without reading every single detail.</li>
    <li><strong>Visualization:</strong> Turn massive datasets into charts and dashboards so humans can understand them quickly.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Example</h5>
  <p>Think about a streaming service like Netflix. Millions of people watch shows every day. 
     By handling Big Data, Netflix can see which shows are popular, recommend movies you might like, 
     and even decide what new series to produce. Without Big Data tools, this would be impossible.</p>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Handling Big Data is like organizing a giant library. You don’t read every book, but you use systems 
     to find the right one fast. With the right tools, Big Data becomes a powerful resource for solving problems 
     and making smarter decisions.</p>

  <p class="fst-italic mt-4">In short, Big Data is about turning overwhelming amounts of information into useful knowledge 
     that helps businesses, governments, and people make better choices.</p>
</div>
""",
 "free": False},
          {"id": 13,
 "title": "Data Communication and Storytelling",
 "description": "Learn to present data effectively through visualizations and narratives.",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Data Communication and Storytelling</h4>
  <p>Data communication is about sharing information in a way people can easily understand. 
     Storytelling means turning numbers into a clear story that connects with your audience. 
     Instead of overwhelming people with spreadsheets, you guide them through the data with visuals 
     and simple explanations that highlight what matters most.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Numbers alone can be hard to remember or interpret. By combining data with storytelling, 
     you make information more engaging and persuasive. A good story helps people see the meaning 
     behind the numbers and inspires action.</p>
  <ul>
    <li><strong>Clarity:</strong> People remember stories better than raw numbers.</li>
    <li><strong>Impact:</strong> A good chart or example can change how decisions are made.</li>
    <li><strong>Connection:</strong> Stories help audiences relate to the data personally.</li>
    <li><strong>Trust:</strong> Clear communication builds confidence in the results.</li>
  </ul>

  <h5 class="fw-bold mt-4">Simple Examples</h5>
  <ul>
    <li>Instead of saying “Sales increased by 20%,” show a line chart that rises like a hill.</li>
    <li>Tell a short story: “Last year, 1 in 5 families struggled with internet access — here’s what that looks like.”</li>
    <li>Use visuals like bar charts or pie charts to make comparisons easy.</li>
    <li>Show before‑and‑after visuals to highlight improvements clearly.</li>
    <li>Use icons or symbols to make data more relatable (like a shopping cart for sales).</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Example</h5>
  <p>Imagine a school presenting exam results. Instead of handing out a table of scores, 
     they show a bar chart comparing average grades across subjects. Then they tell a short story: 
     “Math scores improved by 15% after introducing group study sessions.” This combination of 
     numbers and narrative makes the message clear and memorable.</p>

  <h5 class="fw-bold mt-4">Tips for Effective Storytelling</h5>
  <ul>
    <li>Keep visuals simple and uncluttered.</li>
    <li>Highlight the most important numbers — don’t show everything at once.</li>
    <li>Use comparisons (before vs. after, this year vs. last year) to show change.</li>
    <li>Always explain why the data matters to the audience.</li>
    <li>End with a clear takeaway or action point.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Data storytelling is like being a tour guide. You lead people through the numbers, 
     point out the important sights, and explain why they matter. When done well, 
     data communication transforms raw information into insights that inspire decisions.</p>

  <p class="fst-italic mt-4">In short, storytelling turns data into a journey — one that is clear, 
     memorable, and meaningful for your audience.</p>
</div>
""",
 "free": False},
           {"id": 14,
 "title": "Deep Learning Foundations",
 "description": "Neural networks basics",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Deep Learning Foundations</h4>
  <p>Deep learning is a way of teaching computers to learn from lots of examples, 
     inspired by how our brains work. It uses <strong>neural networks</strong>, which are like 
     layers of decision‑makers stacked together. Each layer looks at part of the problem, 
     passes its result forward, and together they build a strong final answer.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Deep learning powers many of the technologies we use every day. It helps phones recognize faces, 
     apps translate languages, and cars drive themselves. Without deep learning, computers would struggle 
     with complex tasks like understanding speech or identifying objects in pictures.</p>

  <h5 class="fw-bold mt-4">Simple Analogy</h5>
  <p>Imagine a group of people passing notes: the first person looks at a picture and guesses if it’s a cat or dog, 
     then passes their guess to the next person, who refines it, and so on. By the end, the group makes a strong decision together. 
     That’s how layers in a neural network work — each one improves the answer step by step.</p>

  <h5 class="fw-bold mt-4">Key Ideas in Deep Learning</h5>
  <ul>
    <li><strong>Layers:</strong> Information flows through multiple layers, each learning different features (like edges, shapes, or colors in an image).</li>
    <li><strong>Training:</strong> The network learns by adjusting its “weights” based on examples, similar to practice sessions.</li>
    <li><strong>Activation Functions:</strong> These help the network decide which patterns matter most.</li>
    <li><strong>Backpropagation:</strong> A method for correcting mistakes by sending feedback through the layers.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Phones:</strong> Recognizing faces in photos or unlocking with facial recognition.</li>
    <li><strong>Voice Assistants:</strong> Understanding speech and responding to commands.</li>
    <li><strong>Translation Apps:</strong> Converting text or speech into another language automatically.</li>
    <li><strong>Healthcare:</strong> Detecting diseases in medical images like X‑rays or MRIs.</li>
    <li><strong>Transport:</strong> Helping self‑driving cars identify roads, signs, and pedestrians.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Start with simple neural networks before exploring deep ones.</li>
    <li>Use small datasets to practice and understand how training works.</li>
    <li>Visualize how layers transform data step by step.</li>
    <li>Remember: more layers mean more power, but also more complexity.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Deep learning is like building a team of tiny helpers, each focusing on part of the problem, 
     until the whole team solves it. The more examples the network sees, the better it becomes at recognizing patterns. 
     It’s not magic — it’s practice, repetition, and teamwork inside the computer.</p>

  <p class="fst-italic mt-4">In short, deep learning is about stacking simple decision‑makers into powerful networks 
     that can handle complex tasks and make smart predictions.</p>
</div>
""",
 "free": False},
{"id": 15,
 "title": "Capstone Project: End-to-End Workflow",
 "description": "Complete DS project",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Capstone Project: End-to-End Workflow</h4>
  <p>This final project brings everything together. You’ll go through the full 
     data science journey step by step, just like a real‑world project. 
     The goal is to practice all the skills you’ve learned and see how they connect 
     in one complete workflow.</p>

  <h5 class="fw-bold mt-4">What You’ll Do</h5>
  <ul>
    <li><strong>Collect Data:</strong> Find or choose a dataset to work with. This could be sales records, survey results, or open data from the web.</li>
    <li><strong>Clean Data:</strong> Fix errors, remove duplicates, and make it tidy so the information is reliable.</li>
    <li><strong>Explore:</strong> Summarize and visualize the dataset to discover patterns, trends, and unusual values.</li>
    <li><strong>Model:</strong> Try simple predictions (like regression) or groupings (like clustering) to test your ideas.</li>
    <li><strong>Validate:</strong> Check if your model is accurate and reliable using test data and evaluation metrics.</li>
    <li><strong>Communicate:</strong> Share results with clear charts, visuals, and a short story that explains why the findings matter.</li>
    <li><strong>Reflect:</strong> Think about what worked well, what challenges you faced, and how you could improve next time.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Example</h5>
  <p>Imagine you are helping a shop owner. You collect sales data, clean it to remove mistakes, 
     explore it to see which products sell best, build a model to predict future sales, 
     and finally present your findings with charts and a short report. 
     This end‑to‑end process gives the shop owner useful insights to plan ahead.</p>

  <h5 class="fw-bold mt-4">Tips for Success</h5>
  <ul>
    <li>Start small — choose a dataset that is manageable but meaningful.</li>
    <li>Document each step so others can follow your process.</li>
    <li>Use visuals to make your findings clear and engaging.</li>
    <li>Focus on practical insights, not just technical details.</li>
    <li>Remember: the goal is to tell a story with data, not just run code.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>The capstone project is like cooking a full meal: you gather ingredients, prepare them, 
     cook step by step, and finally serve a dish that others can enjoy and understand. 
     By completing this project, you’ll see how data science moves from raw information 
     to useful knowledge that makes a real impact.</p>

  <p class="fst-italic mt-4">In short, the capstone is your chance to put everything together, 
     practice the full workflow, and show that you can turn data into decisions.</p>
</div>
""",
 "free": False},
 ]
    },
    "Statistics": {
        "title": "Statistics",
        "icon": "📈",
        "description": "Master probability, inference, and statistical modeling techniques.",
        "chapters": [
            {"id": 1,
 "title": "Introduction to Statistics",
 "description": "Basic concepts and importance",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Introduction to Statistics</h4>
  <p><strong>Statistics</strong> is the science of learning from data. It helps us collect, organize, and interpret information 
     so we can make better decisions. Instead of guessing, statistics gives us tools to understand patterns and 
     measure uncertainty. It’s like having a flashlight in a dark room — it helps us see clearly where we might 
     otherwise be confused.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Statistics is everywhere in daily life. Governments use it to plan budgets, businesses use it to study customers, 
     and doctors use it to test treatments. Without statistics, we would struggle to make sense of large amounts of 
     information. With it, we can turn data into knowledge and knowledge into action.</p>

  <h5 class="fw-bold mt-4">Key Concepts</h5>
  <ul>
    <li><strong>Data:</strong> The raw information we collect — numbers, words, or observations.</li>
    <li><strong>Population:</strong> The entire group we are interested in (like all students in a school).</li>
    <li><strong>Sample:</strong> A smaller group taken from the population to study (like one class of students).</li>
    <li><strong>Average (Mean):</strong> A simple way to summarize data by finding the central value.</li>
    <li><strong>Variation:</strong> How spread out the data is — do values cluster closely or differ widely?</li>
    <li><strong>Probability:</strong> A measure of how likely something is to happen.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Sports:</strong> Using player statistics to compare performance and predict outcomes.</li>
    <li><strong>Education:</strong> Teachers analyzing test scores to see which topics need more attention.</li>
    <li><strong>Health:</strong> Doctors studying patient data to decide if a new medicine works.</li>
    <li><strong>Business:</strong> Shops tracking sales data to know which products are popular.</li>
    <li><strong>Weather:</strong> Meteorologists using past data to forecast tomorrow’s temperature.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Start with simple summaries like averages and percentages.</li>
    <li>Use graphs and charts to make data easier to understand.</li>
    <li>Remember that samples represent populations — bigger samples usually give better results.</li>
    <li>Think critically: statistics show patterns, but they don’t always explain why.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Statistics is not just about numbers. It’s about asking questions like: 
     “What story does this data tell?” and “How can we use this story to improve decisions?” 
     With statistics, we move from raw data to meaningful insights that guide everyday life.</p>

  <p class="fst-italic mt-4">In short, statistics is the language of data — helping us understand the world 
     more clearly and make smarter choices.</p>
</div>
""",
 "free": True},
            {"id": 2,
 "title": "Descriptive Statistics & Summaries",
 "description": "Mean, median, mode, variance",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Descriptive Statistics & Summaries</h4>
  <p><strong>Descriptive statistics</strong> are tools we use to summarize and describe data. 
     Instead of looking at hundreds of numbers, we use simple measures like averages or spreads 
     to capture the “big picture.” These summaries help us understand what the data is saying 
     without needing to study every single value.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Descriptive statistics make data easier to read and share. Teachers use them to summarize exam results, 
     businesses use them to track sales, and doctors use them to study patient outcomes. 
     Without summaries, raw data can feel overwhelming and confusing.</p>

  <h5 class="fw-bold mt-4">Key Measures</h5>
  <ul>
    <li><strong>Mean (Average):</strong> Add up all the values and divide by the number of items. 
        Example: The average score in a class.</li>
    <li><strong>Median:</strong> The middle value when data is sorted. 
        Example: The middle income in a neighborhood.</li>
    <li><strong>Mode:</strong> The most common value. 
        Example: The shoe size most students wear.</li>
    <li><strong>Range:</strong> The difference between the largest and smallest values.</li>
    <li><strong>Variance & Standard Deviation:</strong> Show how spread out the data is. 
        Example: Do students’ scores cluster closely or vary widely?</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Sports:</strong> A coach looks at the average points scored per game.</li>
    <li><strong>Education:</strong> A teacher checks the median test score to see typical performance.</li>
    <li><strong>Business:</strong> A shop owner finds the mode to know the most popular product size.</li>
    <li><strong>Health:</strong> Doctors measure variance in blood pressure readings to spot unusual cases.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Use the mean when data is balanced, but the median when there are extreme values (outliers).</li>
    <li>Check the mode for categories or repeated values.</li>
    <li>Always look at spread (variance or range) — averages alone can be misleading.</li>
    <li>Visualize with charts (like histograms or box plots) to make summaries clearer.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Descriptive statistics are like a summary of a book. Instead of reading every page, 
     you get the main points quickly. They don’t explain why things happen, 
     but they give a clear snapshot of what the data looks like.</p>

  <p class="fst-italic mt-4">In short, descriptive statistics turn long lists of numbers into simple stories 
     that anyone can understand.</p>
</div>
""",
 "free": True},
           {"id": 3,
 "title": "Probability Fundamentals",
 "description": "Rules and applications of probability",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Probability Fundamentals</h4>
  <p><strong>Probability</strong> is the study of chance. It tells us how likely something is to happen. 
     Instead of guessing, probability gives us a way to measure uncertainty with numbers. 
     For example, saying “there’s a 50% chance of rain” means rain is just as likely as no rain.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Probability is everywhere. Weather forecasts, sports predictions, medical tests, and even games of chance 
     all rely on probability. It helps us make decisions when outcomes are uncertain, 
     turning “maybe” into something we can measure and plan for.</p>

  <h5 class="fw-bold mt-4">Key Rules</h5>
  <ul>
    <li><strong>Probability Scale:</strong> Values range from 0 (impossible) to 1 (certain). 
        Example: The probability of flipping a coin and getting heads is 0.5.</li>
    <li><strong>Addition Rule:</strong> If two events cannot happen at the same time, 
        add their probabilities. Example: Rolling a die and getting a 2 or a 3 = 1/6 + 1/6 = 2/6.</li>
    <li><strong>Multiplication Rule:</strong> If two events are independent, multiply their probabilities. 
        Example: Flipping two coins and both landing heads = 0.5 × 0.5 = 0.25.</li>
    <li><strong>Complement Rule:</strong> The probability of something not happening = 1 minus the probability it does. 
        Example: If chance of rain is 0.3, chance of no rain is 0.7.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Weather:</strong> Forecasts use probability to predict rain or sunshine.</li>
    <li><strong>Sports:</strong> Analysts estimate the chance of a team winning a match.</li>
    <li><strong>Health:</strong> Doctors use probability to measure how likely a treatment will succeed.</li>
    <li><strong>Business:</strong> Shops predict the chance of customers buying certain products.</li>
    <li><strong>Games:</strong> Rolling dice, flipping coins, or drawing cards all follow probability rules.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Always remember probabilities are between 0 and 1 (or 0% to 100%).</li>
    <li>Use fractions or percentages to make probabilities easier to understand.</li>
    <li>Check if events are independent (one doesn’t affect the other) before multiplying probabilities.</li>
    <li>Think of probability as a guide — it doesn’t guarantee outcomes, it measures likelihood.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Probability is about measuring uncertainty. It helps us prepare for the unknown 
     by turning chances into numbers we can work with. Whether predicting the weather, 
     planning a business strategy, or playing a game, probability gives us a way 
     to make smarter choices.</p>

  <p class="fst-italic mt-4">In short, probability is the math of chance — 
     helping us understand risk, make predictions, and deal with uncertainty.</p>
</div>
""",
 "free": True},
           {"id": 4,
 "title": "Random Variables & Distributions",
 "description": "Discrete and continuous distributions",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Random Variables & Distributions</h4>
  <p>A <strong>random variable</strong> is a way of assigning numbers to outcomes of chance events. 
     For example, when you roll a die, the random variable could be the number showing on top. 
     Random variables help us connect real‑world events (like coin flips or test scores) to mathematics 
     so we can study them more easily.</p>

  <h5 class="fw-bold mt-4">Types of Random Variables</h5>
  <ul>
    <li><strong>Discrete Random Variables:</strong> Take specific, separate values. 
        Example: The number of heads when flipping 3 coins (0, 1, 2, or 3).</li>
    <li><strong>Continuous Random Variables:</strong> Can take any value within a range. 
        Example: The exact height of students in a class (like 150.2 cm, 160.8 cm, etc.).</li>
  </ul>

  <h5 class="fw-bold mt-4">What Is a Distribution?</h5>
  <p>A <strong>distribution</strong> shows how likely each value of a random variable is. 
     It’s like a map of probabilities. For a die, each number 1–6 has equal chance (1/6). 
     For student heights, the distribution might show most students around 160 cm, 
     with fewer very short or very tall students.</p>

  <h5 class="fw-bold mt-4">Common Distributions</h5>
  <ul>
    <li><strong>Uniform Distribution:</strong> All outcomes are equally likely (like rolling a fair die).</li>
    <li><strong>Binomial Distribution:</strong> Counts successes in a fixed number of trials (like coin flips).</li>
    <li><strong>Normal Distribution:</strong> The famous “bell curve” where most values cluster around the average.</li>
    <li><strong>Poisson Distribution:</strong> Models rare events happening over time (like number of phone calls per hour).</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Games:</strong> Dice rolls follow a uniform distribution.</li>
    <li><strong>Health:</strong> Human heights often follow a normal distribution.</li>
    <li><strong>Business:</strong> Customer arrivals at a shop can follow a Poisson distribution.</li>
    <li><strong>Education:</strong> Exam scores often form a bell curve, with most students near the average.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Think of random variables as “numbers attached to chance.”</li>
    <li>Discrete = countable values, Continuous = measurable values.</li>
    <li>Distributions tell the story of how values are spread out.</li>
    <li>Visualize distributions with graphs (bar charts for discrete, curves for continuous).</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Random variables and distributions help us describe uncertainty with numbers. 
     They show not just what outcomes are possible, but how likely each one is. 
     This makes them powerful tools for predicting, planning, and understanding patterns in data.</p>

  <p class="fst-italic mt-4">In short, random variables turn chance into numbers, 
     and distributions show the shape of those numbers in the real world.</p>
</div>
""",
 "free": True},
            {"id": 5,
 "title": "Sampling & Data Collection",
 "description": "Methods of sampling",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Sampling & Data Collection</h4>
  <p><strong>Sampling</strong> means selecting a smaller group from a larger population to study. 
     Since it’s often impossible to collect data from everyone, we choose a sample that represents the whole. 
     <strong>Data collection</strong> is the process of gathering information in a structured way so we can analyze it later.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Good sampling and data collection save time, reduce costs, and make studies practical. 
     If done poorly, results can be misleading. For example, asking only one classroom about school meals 
     won’t represent the opinions of the entire school.</p>

  <h5 class="fw-bold mt-4">Common Sampling Methods</h5>
  <ul>
    <li><strong>Random Sampling:</strong> Everyone has an equal chance of being chosen. 
        Example: Picking names from a hat.</li>
    <li><strong>Systematic Sampling:</strong> Select every nth person from a list. 
        Example: Surveying every 10th shopper entering a store.</li>
    <li><strong>Stratified Sampling:</strong> Divide the population into groups (like age or gender) 
        and sample from each group to ensure balance.</li>
    <li><strong>Cluster Sampling:</strong> Choose entire groups at random instead of individuals. 
        Example: Selecting a few schools and surveying all students in them.</li>
    <li><strong>Convenience Sampling:</strong> Use whoever is easiest to reach. 
        Example: Asking friends or nearby people. (Quick but often biased.)</li>
  </ul>

  <h5 class="fw-bold mt-4">Data Collection Methods</h5>
  <ul>
    <li><strong>Surveys & Questionnaires:</strong> Asking people directly through forms or interviews.</li>
    <li><strong>Observation:</strong> Watching and recording behavior or events.</li>
    <li><strong>Experiments:</strong> Testing under controlled conditions to see cause and effect.</li>
    <li><strong>Existing Records:</strong> Using already collected data like census reports or hospital records.</li>
    <li><strong>Digital Tracking:</strong> Collecting data from apps, websites, or sensors.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Education:</strong> A teacher surveys a sample of students to understand study habits.</li>
    <li><strong>Business:</strong> A company collects customer feedback through online forms.</li>
    <li><strong>Healthcare:</strong> Doctors use patient records to study treatment outcomes.</li>
    <li><strong>Transport:</strong> City planners observe traffic flow at selected intersections.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Always aim for a sample that represents the population fairly.</li>
    <li>Be aware of bias — avoid only choosing people who are easy to reach.</li>
    <li>Use clear questions when collecting data to avoid confusion.</li>
    <li>Record data consistently so it can be trusted later.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Sampling and data collection are the foundation of statistics. 
     They determine whether your results are meaningful or misleading. 
     With careful planning, even small samples can reveal big insights.</p>

  <p class="fst-italic mt-4">In short, sampling is about choosing wisely, 
     and data collection is about gathering carefully — together they make analysis possible.</p>
</div>
""",
 "free": True},
            {"id": 6,
 "title": "Hypothesis Testing Basics",
 "description": "Null and alternative hypotheses",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Hypothesis Testing Basics</h4>
  <p><strong>Hypothesis testing</strong> is a way of checking ideas with data. 
     Instead of just assuming something is true, we use evidence to decide. 
     It’s like a courtroom: one side makes a claim, and the other side challenges it. 
     The data acts as the judge to decide which claim is more reasonable.</p>

  <h5 class="fw-bold mt-4">Key Concepts</h5>
  <ul>
    <li><strong>Null Hypothesis (H₀):</strong> The starting assumption — usually that “nothing new is happening.” 
        Example: A new medicine has no effect compared to the old one.</li>
    <li><strong>Alternative Hypothesis (H₁):</strong> The competing idea — that “something is different.” 
        Example: The new medicine works better than the old one.</li>
    <li><strong>Significance Level (α):</strong> The threshold we set to decide if results are strong enough. 
        Commonly 0.05 (5%).</li>
    <li><strong>p‑Value:</strong> A number that tells us how likely our results are if the null hypothesis were true. 
        Small p‑values suggest the null hypothesis may not hold.</li>
    <li><strong>Test Statistic:</strong> A calculated value (like t‑score or z‑score) that helps compare data to expectations.</li>
  </ul>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Hypothesis testing helps us avoid false conclusions. 
     It ensures that decisions are based on evidence, not just guesses. 
     Scientists use it to test new theories, businesses use it to check strategies, 
     and doctors use it to confirm treatments. Without hypothesis testing, 
     we might accept claims that aren’t supported by data.</p>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Education:</strong> A teacher tests if a new teaching method improves exam scores.</li>
    <li><strong>Business:</strong> A company checks if a new advertisement increases sales compared to the old one.</li>
    <li><strong>Healthcare:</strong> Doctors test if a new drug lowers blood pressure more effectively than the current treatment.</li>
    <li><strong>Sports:</strong> Analysts test if a player’s performance has improved after training.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Always state both the null and alternative hypotheses clearly.</li>
    <li>Remember: rejecting H₀ doesn’t prove H₁ is absolutely true — it just means data supports it more.</li>
    <li>Use the p‑value as a guide, not a guarantee.</li>
    <li>Think critically: results can be influenced by sample size, bias, or measurement errors.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Hypothesis testing is about making decisions with data. 
     It gives us a structured way to check claims and avoid being misled. 
     By comparing evidence against expectations, we can decide whether to keep 
     the old assumption or accept a new idea.</p>

  <p class="fst-italic mt-4">In short, hypothesis testing is like giving your idea a fair trial — 
     the data decides if it stands or falls.</p>
</div>
""",
 "free": False},
           {"id": 7,
 "title": "Confidence Intervals & Estimation",
 "description": "Interval estimation methods",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Confidence Intervals & Estimation</h4>
  <p><strong>Estimation</strong> is about using sample data to guess something about the whole population. 
     Instead of giving just one number, we often give a range of values that is likely to contain the true answer. 
     This range is called a <strong>confidence interval</strong>. It shows not only our estimate but also how certain we are about it.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Confidence intervals help us deal with uncertainty. 
     They give us more information than a single number by showing the possible spread of values. 
     For example, instead of saying “the average exam score is 75,” we might say 
     “we are 95% confident the average score is between 72 and 78.” 
     This makes results more reliable and realistic.</p>

  <h5 class="fw-bold mt-4">Key Ideas</h5>
  <ul>
    <li><strong>Point Estimate:</strong> A single best guess (like the sample mean).</li>
    <li><strong>Interval Estimate:</strong> A range of values around the point estimate.</li>
    <li><strong>Confidence Level:</strong> The percentage that shows how sure we are (commonly 90%, 95%, or 99%).</li>
    <li><strong>Margin of Error:</strong> How much the estimate could vary due to sampling.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Surveys:</strong> A poll says a candidate has 52% support, with a margin of error ±3%. 
        This means the true support is likely between 49% and 55%.</li>
    <li><strong>Business:</strong> A shop estimates average daily sales at $500, with a 95% confidence interval of $480–$520.</li>
    <li><strong>Healthcare:</strong> Doctors estimate a new drug lowers blood pressure by 10 points, 
        with a confidence interval of 8–12 points.</li>
    <li><strong>Education:</strong> A teacher estimates the average study time is 2 hours, 
        with a confidence interval of 1.8–2.2 hours.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Remember: a confidence interval is not a guarantee, but a strong estimate.</li>
    <li>Higher confidence levels give wider intervals (more certainty but less precision).</li>
    <li>Larger samples make intervals narrower (more precise estimates).</li>
    <li>Always report both the estimate and the confidence interval together.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Confidence intervals are about showing both the estimate and the uncertainty around it. 
     They make statistics more honest by admitting that we don’t know the exact answer, 
     but we can give a range where the truth is very likely to be. 
     This helps people trust the results and make better decisions.</p>

  <p class="fst-italic mt-4">In short, confidence intervals turn a single guess into a reliable range, 
     helping us measure uncertainty and communicate results clearly.</p>
</div>
""",
 "free": False},
           {"id": 8,
 "title": "Correlation & Regression Analysis",
 "description": "Relationships between variables",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Correlation & Regression Analysis</h4>
  <p><strong>Correlation</strong> and <strong>regression</strong> are tools for studying relationships between variables. 
     Correlation tells us how strongly two things move together, while regression helps us build models 
     to predict one variable based on another. Together, they show us both the strength of a relationship 
     and how we can use it for forecasting.</p>

  <h5 class="fw-bold mt-4">Correlation Basics</h5>
  <p>Correlation is measured with a number called the <strong>correlation coefficient</strong>, 
     which ranges from -1 to +1:</p>
  <ul>
    <li><strong>+1:</strong> Perfect positive relationship (as one goes up, the other goes up).</li>
    <li><strong>-1:</strong> Perfect negative relationship (as one goes up, the other goes down).</li>
    <li><strong>0:</strong> No relationship at all.</li>
  </ul>
  <p>Example: Height and weight often have a positive correlation, while exercise and body fat 
     may show a negative correlation.</p>

  <h5 class="fw-bold mt-4">Regression Basics</h5>
  <p><strong>Regression analysis</strong> goes further by creating an equation to predict outcomes. 
     It draws a line (or curve) through data points to show the relationship between variables.</p>
  <ul>
    <li><strong>Simple Regression:</strong> Uses one variable to predict another. 
        Example: Predicting weight from height.</li>
    <li><strong>Multiple Regression:</strong> Uses two or more variables together. 
        Example: Predicting house prices from size, location, and number of bedrooms.</li>
  </ul>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Correlation and regression help us move beyond guessing. 
     Businesses use them to forecast sales, doctors use them to study health risks, 
     and teachers use them to understand how study time affects exam scores. 
     These tools turn relationships into numbers we can measure and use for decision‑making.</p>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Education:</strong> Study hours and exam scores often show positive correlation.</li>
    <li><strong>Business:</strong> Advertising spend and sales revenue can be modeled with regression.</li>
    <li><strong>Health:</strong> Smoking frequency and lung health often show negative correlation.</li>
    <li><strong>Transport:</strong> Traffic volume and travel time can be predicted using regression models.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Correlation shows strength, but not cause — two things can move together without one causing the other.</li>
    <li>Regression gives predictions, but they are estimates, not guarantees.</li>
    <li>Always visualize data with scatter plots before interpreting correlation or regression.</li>
    <li>Check for outliers — unusual values can distort results.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Correlation tells us how variables move together, 
     and regression builds models to predict outcomes. 
     Together, they help us understand patterns and make smarter decisions 
     in fields ranging from education to healthcare to business.</p>

  <p class="fst-italic mt-4">In short, correlation measures relationships, 
     and regression turns those relationships into useful predictions.</p>
</div>
""",
 "free": False},
           {"id": 9,
 "title": "ANOVA & Comparing Groups",
 "description": "Analysis of variance",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">ANOVA & Comparing Groups</h4>
  <p><strong>ANOVA</strong> stands for <em>Analysis of Variance</em>. 
     It is a statistical method used to compare the averages (means) of three or more groups at once. 
     Instead of running many separate tests, ANOVA gives us one overall test to check 
     if the groups are truly different or if the differences are just due to chance.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>ANOVA is important when we want to compare multiple groups fairly. 
     For example, a teacher may want to know if students in different classes score differently, 
     or a company may want to test if three marketing strategies lead to different sales results. 
     Without ANOVA, we might run many tests and increase the risk of false conclusions.</p>

  <h5 class="fw-bold mt-4">Key Ideas</h5>
  <ul>
    <li><strong>Groups:</strong> The categories we are comparing (like Class A, Class B, Class C).</li>
    <li><strong>Mean:</strong> The average score or value in each group.</li>
    <li><strong>Variance:</strong> How spread out the data is within each group.</li>
    <li><strong>F‑Test:</strong> The main test statistic in ANOVA that compares differences between groups to differences within groups.</li>
    <li><strong>Assumptions:</strong> ANOVA works best when data is normally distributed, groups have similar variances, and samples are independent.</li>
  </ul>

  <h5 class="fw-bold mt-4">Post‑Hoc Comparisons</h5>
  <p>If ANOVA shows that at least one group is different, we still need to find out which ones. 
     <strong>Post‑hoc tests</strong> (like Tukey’s test) are used after ANOVA to compare groups pair by pair. 
     This helps us see exactly where the differences lie.</p>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Education:</strong> Comparing average exam scores across three different teaching methods.</li>
    <li><strong>Business:</strong> Testing if three advertising campaigns lead to different levels of sales.</li>
    <li><strong>Healthcare:</strong> Checking if three diets result in different average weight loss.</li>
    <li><strong>Sports:</strong> Comparing training programs to see which produces the best performance improvements.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Use ANOVA when comparing three or more groups — for two groups, a t‑test is enough.</li>
    <li>Check assumptions first (normality, equal variances, independence).</li>
    <li>Remember: ANOVA tells you if differences exist, but post‑hoc tests show where they are.</li>
    <li>Visualize group means with bar charts or box plots to make results clearer.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>ANOVA is about comparing averages across multiple groups in one fair test. 
     It helps us avoid false conclusions and gives a clear picture of whether differences are real. 
     By combining ANOVA with post‑hoc tests, we can understand both the overall result 
     and the specific group differences.</p>

  <p class="fst-italic mt-4">In short, ANOVA is like a referee — it checks if the groups are playing differently, 
     and post‑hoc tests show exactly which teams stand out.</p>
</div>
""",
 "free": False},
            {"id": 10,
 "title": "Nonparametric Methods",
 "description": "Tests without distribution assumptions",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Nonparametric Methods</h4>
  <p><strong>Nonparametric methods</strong> are statistical tests that do not assume data follows a normal distribution. 
     They are especially useful when data is skewed, contains outliers, or is measured in ranks instead of precise numbers. 
     Think of them as flexible tools that work even when the usual rules about “bell‑shaped curves” don’t apply.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Many real‑world datasets don’t fit the neat assumptions of parametric tests. 
     For example, income data is often skewed, and survey responses may be ranked (like 1st, 2nd, 3rd choice). 
     Nonparametric methods allow us to analyze such data fairly without forcing it into shapes it doesn’t have.</p>

  <h5 class="fw-bold mt-4">Key Nonparametric Tests</h5>
  <ul>
    <li><strong>Mann‑Whitney U Test:</strong> Compares two independent groups when data is not normally distributed. 
        Example: Comparing customer satisfaction scores between two stores.</li>
    <li><strong>Kruskal‑Wallis Test:</strong> Extends the Mann‑Whitney test to more than two groups. 
        Example: Comparing median exam scores across three different teaching methods.</li>
    <li><strong>Wilcoxon Signed‑Rank Test:</strong> Compares two related samples (like before‑and‑after measurements). 
        Example: Checking if blood pressure changes after treatment.</li>
    <li><strong>Chi‑Square Test:</strong> Tests relationships between categories. 
        Example: Checking if product preference differs by age group.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Healthcare:</strong> Doctors compare patient outcomes when data is not normally distributed.</li>
    <li><strong>Business:</strong> Companies analyze customer rankings of products using nonparametric tests.</li>
    <li><strong>Education:</strong> Teachers compare class performance when scores are unevenly spread.</li>
    <li><strong>Social Science:</strong> Researchers study survey responses that use “agree/disagree” scales.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Use nonparametric tests when data is skewed, ordinal (ranked), or has outliers.</li>
    <li>Remember: these tests often compare medians or ranks, not means.</li>
    <li>Nonparametric methods are less powerful than parametric ones when assumptions are met, 
        but they are safer when assumptions are broken.</li>
    <li>Visualize data first — if it doesn’t look normal, consider a nonparametric approach.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Nonparametric methods are flexible tools for analyzing messy or unusual data. 
     They don’t rely on strict distribution rules, making them practical for real‑world problems. 
     By using these methods, we can still draw meaningful conclusions even when data refuses to fit the “normal” mold.</p>

  <p class="fst-italic mt-4">In short, nonparametric methods are like backup tools — 
     they step in when standard tests don’t work, helping us keep analysis fair and reliable.</p>
</div>
""",
 "free": False},
            {"id": 11,
 "title": "Bayesian Statistics Introduction",
 "description": "Bayes theorem and applications",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Bayesian Statistics Introduction</h4>
  <p><strong>Bayesian statistics</strong> is a way of thinking about probability that focuses on updating our beliefs 
     when new evidence appears. Instead of treating probability as fixed, Bayesian methods treat it as something 
     that changes as we learn more. This makes it powerful for real‑world problems where information arrives step by step.</p>

  <h5 class="fw-bold mt-4">Bayes’ Theorem</h5>
  <p>Bayes’ theorem is the rule that tells us how to update probabilities. 
     It combines what we already believe (called the <strong>prior</strong>) with new data (the <strong>likelihood</strong>) 
     to produce an updated belief (the <strong>posterior</strong>).</p>
  <p><em>Posterior = (Prior × Likelihood) ÷ Evidence</em></p>
  <p>Think of it as a recipe: start with your initial belief, mix in the new evidence, 
     and get a refined belief that better reflects reality.</p>

  <h5 class="fw-bold mt-4">Key Concepts</h5>
  <ul>
    <li><strong>Prior:</strong> What you believe before seeing new data. Example: You think there’s a 10% chance it will rain tomorrow.</li>
    <li><strong>Likelihood:</strong> How well the new data fits different possibilities. Example: The weather forecast shows clouds, which makes rain more likely.</li>
    <li><strong>Posterior:</strong> Your updated belief after combining prior and evidence. Example: Now you believe there’s a 40% chance of rain.</li>
  </ul>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Bayesian methods are useful because they allow us to keep learning as new information arrives. 
     Doctors use them to update diagnoses when new test results come in, businesses use them to adjust forecasts 
     when markets change, and scientists use them to refine theories as experiments provide more evidence.</p>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Healthcare:</strong> A doctor starts with a prior belief about a disease, then updates it after seeing test results.</li>
    <li><strong>Spam Filters:</strong> Email systems update the probability that a message is spam based on words inside it.</li>
    <li><strong>Sports:</strong> Analysts update predictions about a team’s chances of winning as the game progresses.</li>
    <li><strong>Business:</strong> Companies update sales forecasts as new customer data arrives.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Think of probability as belief, not just chance.</li>
    <li>Start with a prior, then adjust it when new evidence appears.</li>
    <li>Bayesian methods are especially useful when data is limited or arrives gradually.</li>
    <li>Visualize priors and posteriors with graphs to see how beliefs shift.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Bayesian statistics is about learning from evidence. 
     It gives us a structured way to update our beliefs and make smarter decisions in uncertain situations. 
     Instead of sticking to one fixed probability, we keep adjusting as new information comes in.</p>

  <p class="fst-italic mt-4">In short, Bayesian statistics is like detective work — 
     you start with a hunch, gather clues, and update your conclusion as the story unfolds.</p>
</div>
""",
 "free": False},
            {"id": 12,
 "title": "Multivariate Statistics",
 "description": "Multiple variables analysis",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Multivariate Statistics</h4>
  <p><strong>Multivariate statistics</strong> are methods used to analyze data that has more than one variable at the same time. 
     Instead of looking at each variable separately, we study how they interact together. 
     This is important because real‑world problems often involve many factors working at once.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Most datasets are complex. For example, a student’s exam score may depend on study hours, sleep, and motivation. 
     Businesses track sales based on price, advertising, and customer demographics. 
     Multivariate statistics help us see the bigger picture by analyzing several variables together, 
     revealing patterns that single‑variable methods might miss.</p>

  <h5 class="fw-bold mt-4">Key Techniques</h5>
  <ul>
    <li><strong>Principal Component Analysis (PCA):</strong> Simplifies large datasets by finding the main directions of variation. 
        Example: Reducing dozens of survey questions into a few key “factors” that explain most differences.</li>
    <li><strong>Factor Analysis:</strong> Groups related variables together to uncover hidden patterns. 
        Example: In psychology, grouping questions about mood, energy, and focus into one factor called “well‑being.”</li>
    <li><strong>Multiple Regression:</strong> Predicts an outcome using several predictors at once. 
        Example: Estimating house prices using size, location, and number of bedrooms.</li>
    <li><strong>Cluster Analysis:</strong> Groups observations into categories based on similarities. 
        Example: Segmenting customers into groups based on shopping habits.</li>
    <li><strong>Discriminant Analysis:</strong> Classifies data into predefined groups. 
        Example: Sorting plants into species based on multiple measurements.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Education:</strong> Understanding how study time, attendance, and motivation together affect exam scores.</li>
    <li><strong>Business:</strong> Analyzing how price, advertising, and customer age influence product sales.</li>
    <li><strong>Healthcare:</strong> Studying how diet, exercise, and genetics combine to affect health outcomes.</li>
    <li><strong>Social Science:</strong> Exploring how income, education, and location together shape lifestyle choices.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Start with visualization — scatter plots, heatmaps, or PCA plots make relationships clearer.</li>
    <li>Remember: multivariate methods simplify complexity, but interpretation still requires careful thought.</li>
    <li>Check assumptions — some methods (like regression) need data to meet certain conditions.</li>
    <li>Use multivariate analysis when variables are connected, not isolated.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Multivariate statistics help us move beyond one‑variable thinking. 
     They allow us to see how multiple factors interact, uncover hidden structures, 
     and make better predictions. By combining techniques like PCA, regression, and clustering, 
     we can turn complex datasets into clear insights.</p>

  <p class="fst-italic mt-4">In short, multivariate statistics are about understanding the whole story — 
     not just one chapter — of your data.</p>
</div>
""",
 "free": False},
            {"id": 13,
 "title": "Time Series Analysis",
 "description": "Forecasting and trends",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Time Series Analysis</h4>
  <p><strong>Time series analysis</strong> is the study of data collected over time. 
     Instead of looking at numbers in isolation, we focus on how they change from one moment to the next. 
     This helps us spot patterns, understand trends, and make forecasts about the future.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Many important datasets are time‑based: daily temperatures, monthly sales, yearly exam scores, or hourly traffic counts. 
     By analyzing these sequences, we can predict what might happen next and plan ahead. 
     Businesses use time series to forecast demand, governments use it to plan budgets, 
     and scientists use it to study climate change.</p>

  <h5 class="fw-bold mt-4">Key Concepts</h5>
  <ul>
    <li><strong>Trend:</strong> The long‑term direction of data (e.g., sales increasing over years).</li>
    <li><strong>Seasonality:</strong> Regular patterns that repeat (e.g., ice cream sales rising every summer).</li>
    <li><strong>Cyclic Patterns:</strong> Longer‑term ups and downs (e.g., economic cycles).</li>
    <li><strong>Noise:</strong> Random fluctuations that don’t follow a clear pattern.</li>
  </ul>

  <h5 class="fw-bold mt-4">Common Methods</h5>
  <ul>
    <li><strong>Moving Averages:</strong> Smooth out short‑term ups and downs to highlight overall trends.</li>
    <li><strong>Exponential Smoothing:</strong> Gives more weight to recent data when forecasting.</li>
    <li><strong>ARIMA Models:</strong> Advanced models that combine past values and errors to predict future points.</li>
    <li><strong>Trend Forecasting:</strong> Extends current patterns into the future to estimate what might happen next.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Weather:</strong> Forecasting tomorrow’s temperature based on past records.</li>
    <li><strong>Business:</strong> Predicting next month’s sales from historical data.</li>
    <li><strong>Transport:</strong> Estimating traffic flow at rush hour using past trends.</li>
    <li><strong>Education:</strong> Tracking student performance over semesters to see improvement or decline.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Always plot your data first — graphs make patterns easier to see.</li>
    <li>Look for seasonality and trends before choosing a forecasting method.</li>
    <li>Start simple (like moving averages) before using advanced models like ARIMA.</li>
    <li>Remember: forecasts are estimates, not guarantees — unexpected events can change outcomes.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Time series analysis is about learning from the past to prepare for the future. 
     By studying how data changes over time, we can identify trends, spot repeating patterns, 
     and make informed predictions. This makes time series one of the most practical tools in statistics.</p>

  <p class="fst-italic mt-4">In short, time series turns history into a guidebook — 
     helping us see what’s coming next.</p>
</div>
""",
 "free": False},
            {"id": 14,
 "title": "Statistical Modeling in Practice",
 "description": "Applied modeling techniques",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Statistical Modeling in Practice</h4>
  <p><strong>Statistical modeling</strong> is about using mathematics to describe real‑world problems. 
     Instead of just looking at raw data, we build models that capture relationships between variables 
     and help us make predictions or decisions. In practice, modeling is less about perfect formulas 
     and more about choosing the right tool for the job.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Models are used everywhere: businesses forecast sales, doctors predict health outcomes, 
     and governments plan budgets. A good model simplifies reality enough to be useful, 
     but still captures the key patterns. The challenge is balancing simplicity with accuracy.</p>

  <h5 class="fw-bold mt-4">Steps in Applied Modeling</h5>
  <ul>
    <li><strong>Define the Problem:</strong> Clearly state what you want to predict or explain.</li>
    <li><strong>Select Variables:</strong> Choose the factors that matter most for the problem.</li>
    <li><strong>Pick a Model:</strong> Decide whether regression, classification, or another method fits best.</li>
    <li><strong>Fit the Model:</strong> Use data to train the model and estimate parameters.</li>
    <li><strong>Check Diagnostics:</strong> Test if the model’s assumptions hold and if predictions make sense.</li>
    <li><strong>Interpret Results:</strong> Translate numbers into insights that non‑experts can understand.</li>
    <li><strong>Refine:</strong> Adjust or try new models if the first one doesn’t perform well.</li>
  </ul>

  <h5 class="fw-bold mt-4">Model Selection</h5>
  <p>Choosing the right model depends on the data and the question. 
     Simple models are easier to explain, while complex models may capture more detail. 
     Tools like cross‑validation help compare models fairly to see which one works best.</p>

  <h5 class="fw-bold mt-4">Diagnostics</h5>
  <p>Diagnostics are checks to make sure the model is reliable. 
     They include looking at residuals (differences between predicted and actual values), 
     testing assumptions (like normality or independence), and checking for overfitting 
     (when a model memorizes instead of learning).</p>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Business:</strong> Predicting sales based on advertising spend, season, and customer demographics.</li>
    <li><strong>Healthcare:</strong> Modeling patient recovery times using age, treatment type, and lifestyle factors.</li>
    <li><strong>Education:</strong> Estimating exam scores from study hours, attendance, and prior performance.</li>
    <li><strong>Transport:</strong> Forecasting traffic congestion using time of day, weather, and road conditions.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Start simple — complex models aren’t always better.</li>
    <li>Always check assumptions before trusting results.</li>
    <li>Use visuals (plots of residuals, fitted lines) to understand model behavior.</li>
    <li>Interpret results in plain language — numbers should tell a clear story.</li>
    <li>Remember: models are guides, not crystal balls. They help us make informed decisions, not perfect predictions.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Statistical modeling in practice is about applying the right techniques to real problems. 
     It’s not just about math — it’s about asking good questions, checking assumptions, 
     and turning results into insights that matter. A well‑chosen model can guide decisions, 
     reduce uncertainty, and reveal patterns hidden in data.</p>

  <p class="fst-italic mt-4">In short, statistical modeling is the bridge between raw data and practical decisions — 
     helping us move from numbers to knowledge.</p>
</div>
""",
 "free": False},
            {"id": 15,
 "title": "Capstone Project: Statistical Report Example",
 "description": "Complete statistical analysis project",
 "content": """
<div style="background-color:#002b36; color:#d6e1e9; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Capstone Project: Statistical Report Example</h4>
  <p>This capstone project brings together everything you have learned in the course. 
     The goal is to conduct a complete statistical analysis — from collecting data 
     to writing a professional report. By the end, you will see how descriptive statistics, 
     inference, regression, and clear communication all fit together in practice.</p>

  <h5 class="fw-bold mt-4">Step 1: Define the Question</h5>
  <p>Start by asking a clear question. For example: 
     “Does study time affect exam scores?” or “Do different marketing strategies 
     lead to different sales results?” A good project begins with a focused problem.</p>

  <h5 class="fw-bold mt-4">Step 2: Collect Data</h5>
  <p>Gather information that relates to your question. 
     This could be survey responses, sales records, health measurements, or any dataset 
     you can access. Make sure the data is reliable and relevant.</p>

  <h5 class="fw-bold mt-4">Step 3: Clean and Organize Data</h5>
  <p>Check for missing values, errors, or outliers. 
     Organize the dataset so it is ready for analysis. 
     Clean data ensures that your results are trustworthy.</p>

  <h5 class="fw-bold mt-4">Step 4: Apply Descriptive Statistics</h5>
  <p>Summarize the data with measures like mean, median, mode, and variance. 
     Use charts and tables to make patterns easy to see. 
     This gives readers a quick overview of the dataset.</p>

  <h5 class="fw-bold mt-4">Step 5: Conduct Inference</h5>
  <p>Use hypothesis testing or confidence intervals to draw conclusions about the population. 
     For example, test whether two groups have different averages or estimate the range 
     where the true mean lies.</p>

  <h5 class="fw-bold mt-4">Step 6: Build Regression Models</h5>
  <p>Apply regression analysis to study relationships between variables. 
     For example, predict exam scores based on study hours, or forecast sales 
     using advertising spend and customer demographics. 
     Interpret coefficients in plain language so results are easy to understand.</p>

  <h5 class="fw-bold mt-4">Step 7: Interpret Results</h5>
  <p>Translate numbers into insights. 
     Instead of just reporting “the mean is 75,” explain what it means: 
     “On average, students who studied more scored higher.” 
     Focus on clarity and practical meaning.</p>

  <h5 class="fw-bold mt-4">Step 8: Write the Report</h5>
  <p>Present findings in a professional format. 
     Include an introduction, methods, results, and conclusion. 
     Use visuals like graphs and tables to support your points. 
     Keep the language simple so non‑experts can follow along.</p>

  <h5 class="fw-bold mt-4">Everyday Example</h5>
  <p>Imagine a small business owner wants to know if advertising increases sales. 
     They collect monthly sales data, apply descriptive statistics to summarize it, 
     run a regression to see the effect of advertising spend, 
     and write a report showing that sales rise when advertising increases. 
     This is a complete statistical project in action.</p>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Keep the question simple and clear.</li>
    <li>Use visuals to make results easy to understand.</li>
    <li>Explain findings in plain language, not just numbers.</li>
    <li>Practice writing reports — communication is as important as analysis.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>The capstone project shows how all the pieces of statistics fit together. 
     From data collection to reporting, you learn to apply methods in a real‑world context. 
     This final step prepares you to use statistics confidently in your own work or studies.</p>

  <p class="fst-italic mt-4">In short, the capstone project is your chance to put theory into practice — 
     turning data into decisions and reports into real impact.</p>
</div>
""",
 "free": False},
        ]
    },
"R Programming": {
    "title": "R Programming",
    "icon": "💻",
    "description": "Build reproducible workflows and powerful analytics with R.",
    "chapters": [
        {"id": 1,
 "title": "Introduction to R & RStudio",
 "description": "Getting started with R environment",
 "content": """
<div style="background-color:#002b36; color:#e0f7fa; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Introduction to R & RStudio</h4>
  <p><strong>R</strong> is a programming language designed for statistics and data analysis. 
     <strong>RStudio</strong> is a friendly interface that makes working with R easier. 
     Together, they give you a powerful environment to explore data, run analyses, 
     and create visualizations.</p>

  <h5 class="fw-bold mt-4">Step 1: Install R and RStudio</h5>
  <p>To begin, download and install R (the language) and RStudio (the interface). 
     R does the calculations, while RStudio provides a clean workspace with menus, 
     tabs, and tools that make coding simpler.</p>

  <h5 class="fw-bold mt-4">Step 2: Explore the R Console</h5>
  <p>The console is where you type commands and see results instantly. 
     For example, typing <code>2 + 2</code> will return <code>4</code>. 
     This is the quickest way to test ideas and learn the basics.</p>

  <h5 class="fw-bold mt-4">Step 3: Use the Script Editor</h5>
  <p>Instead of typing everything directly into the console, 
     you can write longer sets of instructions in the script editor. 
     This makes your work reusable and easier to share. 
     Think of it as writing a recipe that R can follow step by step.</p>

  <h5 class="fw-bold mt-4">Step 4: Manage Your Workspace</h5>
  <p>The workspace keeps track of the data and variables you are using. 
     You can clear it, save it, or reload it later. 
     This helps you stay organized as projects grow.</p>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Education:</strong> Students use RStudio to practice statistics homework.</li>
    <li><strong>Business:</strong> Analysts explore sales data to find trends.</li>
    <li><strong>Healthcare:</strong> Researchers study patient records to discover patterns.</li>
    <li><strong>Science:</strong> Scientists use R to analyze experiments and visualize results.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Start small — try simple commands in the console.</li>
    <li>Save your scripts so you don’t lose progress.</li>
    <li>Use comments (with <code>#</code>) to explain your code.</li>
    <li>Don’t worry about mistakes — errors are part of learning.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>R and RStudio together create a powerful environment for learning statistics and data analysis. 
     By starting with simple commands and gradually building scripts, 
     you’ll gain confidence and be ready to tackle bigger projects.</p>

  <p class="fst-italic mt-4">In short, R is the engine, and RStudio is the dashboard — 
     together they make data analysis smooth and approachable.</p>
</div>
""",
 "free": True},
        {"id": 2,
 "title": "Data Types & Structures in R",
 "description": "Vectors, lists, data frames",
 "content": """
<div style="background-color:#002b36; color:#e0f7fa; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Data Types & Structures in R</h4>
  <p>In R, data is stored in different <strong>structures</strong>. 
     These structures are the building blocks of programming in R. 
     Understanding them is the first step toward working with datasets efficiently.</p>

  <h5 class="fw-bold mt-4">Basic Data Types</h5>
  <ul>
    <li><strong>Numeric:</strong> Numbers like 3.14 or 42.</li>
    <li><strong>Character:</strong> Text values like "Hello" or "RStudio".</li>
    <li><strong>Logical:</strong> TRUE or FALSE values used for conditions.</li>
    <li><strong>Integer:</strong> Whole numbers like 5 or 100.</li>
    <li><strong>Factor:</strong> Categories such as "Male" and "Female".</li>
  </ul>

  <h5 class="fw-bold mt-4">Key Data Structures</h5>
  <ul>
    <li><strong>Vectors:</strong> A sequence of values of the same type. 
        Example: <code>c(1, 2, 3, 4)</code>.</li>
    <li><strong>Lists:</strong> A flexible container that can hold different types. 
        Example: a list with numbers, text, and even another list.</li>
    <li><strong>Matrices:</strong> A table of numbers arranged in rows and columns. 
        Example: a 3×3 matrix of exam scores.</li>
    <li><strong>Data Frames:</strong> The most common structure for datasets. 
        Each column can hold a different type (numbers, text, categories). 
        Example: a table of students with names, ages, and grades.</li>
  </ul>

  <h5 class="fw-bold mt-4">Accessing Elements</h5>
  <p>You can pick out specific parts of these structures using indexes:</p>
  <ul>
    <li><strong>Vectors:</strong> <code>x[2]</code> gives the second element.</li>
    <li><strong>Lists:</strong> <code>mylist[[1]]</code> gives the first item.</li>
    <li><strong>Matrices:</strong> <code>m[2,3]</code> gives the value in row 2, column 3.</li>
    <li><strong>Data Frames:</strong> <code>df$age</code> gives the “age” column.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Education:</strong> A vector of student scores.</li>
    <li><strong>Business:</strong> A data frame of products with price and quantity.</li>
    <li><strong>Healthcare:</strong> A matrix of patient test results.</li>
    <li><strong>Research:</strong> A list combining survey responses and notes.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Start with vectors — they are the simplest structure.</li>
    <li>Use data frames for real datasets — they are the most practical.</li>
    <li>Practice accessing elements with brackets <code>[]</code> and the <code>$</code> symbol.</li>
    <li>Remember: lists are flexible, but data frames are organized.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Data types and structures are the foundation of R programming. 
     By learning how to store, organize, and access data, 
     you gain the tools to handle any dataset. 
     Once you master these basics, you’ll be ready to explore more advanced analysis.</p>

  <p class="fst-italic mt-4">In short, data structures are like containers — 
     vectors hold simple items, lists hold mixed items, 
     matrices hold tables, and data frames hold real‑world datasets.</p>
</div>
""",
 "free": True},
        {"id": 3,
 "title": "Importing & Cleaning Data in R",
 "description": "Read and clean datasets",
 "content": """
<div style="background-color:#002b36; color:#e0f7fa; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Importing & Cleaning Data in R</h4>
  <p>Data analysis begins with bringing data into R and preparing it for use. 
     Raw datasets often contain missing values, duplicates, or inconsistent formats. 
     Learning how to import and clean data ensures that your analysis is accurate and reliable.</p>

  <h5 class="fw-bold mt-4">Step 1: Importing Data</h5>
  <p>R can read many file types. The most common are CSV, Excel, and text files:</p>
  <ul>
    <li><strong>CSV Files:</strong> Use <code>read.csv("file.csv")</code> to load comma‑separated data.</li>
    <li><strong>Excel Files:</strong> Use the <code>readxl</code> package with <code>read_excel("file.xlsx")</code>.</li>
    <li><strong>Text Files:</strong> Use <code>read.table("file.txt")</code> for space‑ or tab‑separated data.</li>
  </ul>
  <p>Tip: Always check the first few rows with <code>head(data)</code> to confirm the import worked correctly.</p>

  <h5 class="fw-bold mt-4">Step 2: Exploring the Dataset</h5>
  <p>Before cleaning, explore the data:</p>
  <ul>
    <li><code>str(data)</code> shows the structure of the dataset.</li>
    <li><code>summary(data)</code> gives quick statistics for each column.</li>
    <li><code>names(data)</code> lists the column names.</li>
  </ul>

  <h5 class="fw-bold mt-4">Step 3: Cleaning Data</h5>
  <p>Cleaning ensures your dataset is ready for analysis:</p>
  <ul>
    <li><strong>Handling Missing Values:</strong> Use <code>na.omit(data)</code> to remove rows with missing values, 
        or replace them with averages using <code>ifelse(is.na(x), mean(x, na.rm=TRUE), x)</code>.</li>
    <li><strong>Removing Duplicates:</strong> Use <code>unique(data)</code> or <code>duplicated()</code> to check and drop duplicates.</li>
    <li><strong>Fixing Formats:</strong> Convert text to numbers with <code>as.numeric()</code>, 
        or dates with <code>as.Date()</code>.</li>
    <li><strong>Renaming Columns:</strong> Use <code>colnames(data)</code> to make names clear and consistent.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Business:</strong> Import sales records from Excel and clean missing entries.</li>
    <li><strong>Education:</strong> Load student exam scores from CSV and remove duplicate rows.</li>
    <li><strong>Healthcare:</strong> Import patient data and fix inconsistent date formats.</li>
    <li><strong>Research:</strong> Clean survey responses by handling skipped questions.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Always explore the dataset before cleaning — know what you’re working with.</li>
    <li>Keep a copy of the raw data so you don’t lose original information.</li>
    <li>Document your cleaning steps in scripts for reproducibility.</li>
    <li>Start simple: handle missing values and duplicates first, then move to formatting issues.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Importing and cleaning data is the foundation of analysis. 
     Clean data leads to trustworthy results, while messy data can mislead. 
     By mastering these steps, you ensure that your work in R is accurate, 
     reproducible, and ready for deeper exploration.</p>

  <p class="fst-italic mt-4">In short, importing brings data into R, 
     and cleaning makes it usable — together they prepare your dataset for success.</p>
</div>
""",
 "free": True},
        {"id": 4,
 "title": "Data Manipulation",
 "description": "Filter, group, summarize data",
 "content": """
<div style="background-color:#002b36; color:#e0f7fa; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Data Manipulation</h4>
  <p><strong>Data manipulation</strong> means reshaping and transforming datasets so they are easier to analyze. 
     In R, the <code>dplyr</code> package provides simple and powerful functions to filter, select, group, 
     and summarize data. These tools help you focus on the information that matters most.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Raw datasets are often large and messy. By filtering rows, selecting columns, and summarizing values, 
     you can uncover insights quickly. Data manipulation is like cleaning and organizing your desk — 
     once everything is in order, it’s easier to work productively.</p>

  <h5 class="fw-bold mt-4">Key Functions in dplyr</h5>
  <ul>
    <li><strong>filter():</strong> Pick rows that meet certain conditions. 
        Example: <code>filter(data, age > 18)</code> selects only adults.</li>
    <li><strong>select():</strong> Choose specific columns. 
        Example: <code>select(data, name, score)</code> keeps only names and scores.</li>
    <li><strong>mutate():</strong> Create new columns or modify existing ones. 
        Example: <code>mutate(data, grade = score/10)</code> adds a grade column.</li>
    <li><strong>group_by():</strong> Organize data into groups. 
        Example: <code>group_by(data, class)</code> groups students by class.</li>
    <li><strong>summarize():</strong> Calculate summary statistics for each group. 
        Example: <code>summarize(data, avg_score = mean(score))</code> gives average scores per class.</li>
  </ul>

  <h5 class="fw-bold mt-4">Step-by-Step Example</h5>
  <p>Imagine you have a dataset of students with columns for name, class, and score:</p>
  <ol>
    <li>Use <code>select()</code> to keep only class and score.</li>
    <li>Use <code>filter()</code> to keep scores above 50.</li>
    <li>Use <code>group_by()</code> to group by class.</li>
    <li>Use <code>summarize()</code> to calculate the average score per class.</li>
  </ol>
  <p>This workflow quickly shows which class is performing best.</p>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Business:</strong> Filter sales data to focus on one region, then summarize total revenue.</li>
    <li><strong>Education:</strong> Group exam scores by subject and calculate average performance.</li>
    <li><strong>Healthcare:</strong> Select patient records, filter by age group, and summarize average blood pressure.</li>
    <li><strong>Research:</strong> Mutate datasets to add new calculated variables like growth rates.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Think of <code>filter()</code> as choosing rows and <code>select()</code> as choosing columns.</li>
    <li>Use <code>mutate()</code> to add new insights without changing the original data.</li>
    <li>Always combine <code>group_by()</code> with <code>summarize()</code> to see grouped results.</li>
    <li>Chain functions together with the pipe operator <code>%>%</code> for smooth workflows.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Data manipulation is about transforming raw data into meaningful insights. 
     By filtering, selecting, mutating, grouping, and summarizing, 
     you can answer questions quickly and clearly. These tools make R a powerful ally 
     for anyone working with data.</p>

  <p class="fst-italic mt-4">In short, data manipulation is like shaping clay — 
     you mold raw data into useful forms that reveal the story inside.</p>
</div>
""",
 "free": True},
        {"id": 5,
 "title": "Data Visualization with ggplot2",
 "description": "Create plots and charts",
 "content": """
<div style="background-color:#002b36; color:#e0f7fa; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Data Visualization with ggplot2</h4>
  <p><strong>Data visualization</strong> is about turning numbers into pictures that tell a story. 
     In R, the <code>ggplot2</code> package is one of the most powerful and flexible tools 
     for creating professional charts. It helps you see patterns, trends, and relationships 
     that are hidden in raw data.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Charts and graphs make data easier to understand. 
     A single plot can explain what thousands of numbers mean. 
     Businesses use them to show sales trends, teachers use them to explain exam results, 
     and scientists use them to present discoveries. 
     With ggplot2, you can create visuals that are both clear and attractive.</p>

  <h5 class="fw-bold mt-4">Key Concepts in ggplot2</h5>
  <ul>
    <li><strong>Aesthetics (aes):</strong> Define how data is mapped to visuals, such as x‑axis, y‑axis, color, or size.</li>
    <li><strong>Geoms:</strong> The shapes used to display data (bars, points, lines, etc.).</li>
    <li><strong>Layers:</strong> Build plots step by step by adding geoms, labels, and adjustments.</li>
    <li><strong>Themes:</strong> Control the overall look of the plot (fonts, backgrounds, gridlines).</li>
  </ul>

  <h5 class="fw-bold mt-4">Common Plot Types</h5>
  <ul>
    <li><strong>Bar Charts:</strong> Compare categories. Example: sales by product type.</li>
    <li><strong>Scatter Plots:</strong> Show relationships between two variables. Example: height vs. weight.</li>
    <li><strong>Line Graphs:</strong> Display trends over time. Example: monthly revenue growth.</li>
    <li><strong>Histograms:</strong> Show the distribution of a single variable. Example: exam score frequencies.</li>
  </ul>

  <h5 class="fw-bold mt-4">Step-by-Step Example</h5>
  <p>Imagine you have a dataset of students with scores:</p>
  <ol>
    <li>Start with <code>ggplot(data, aes(x = score))</code> to set up the plot.</li>
    <li>Add <code>geom_histogram()</code> to create a histogram of scores.</li>
    <li>Customize with <code>theme_minimal()</code> for a clean look.</li>
    <li>Add labels with <code>labs(title = "Exam Score Distribution")</code>.</li>
  </ol>
  <p>This simple workflow produces a polished chart that communicates clearly.</p>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Business:</strong> Visualize monthly sales with line graphs.</li>
    <li><strong>Education:</strong> Show class performance with bar charts.</li>
    <li><strong>Healthcare:</strong> Plot patient age vs. blood pressure with scatter plots.</li>
    <li><strong>Research:</strong> Display distributions of survey responses with histograms.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Start with simple plots, then add layers gradually.</li>
    <li>Use themes to make charts look professional with minimal effort.</li>
    <li>Always label axes and titles so the chart tells a clear story.</li>
    <li>Experiment with colors and shapes to highlight important points.</li>
    <li>Remember: visuals should explain data, not confuse — keep them clean and simple.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>ggplot2 makes visualization flexible and powerful. 
     By combining aesthetics, geoms, layers, and themes, 
     you can create charts that not only display data but also explain it. 
     Visualization is about communication — turning data into insights that everyone can understand.</p>

  <p class="fst-italic mt-4">In short, ggplot2 is like a painter’s toolkit — 
     you choose the canvas, add layers, and create visuals that bring data to life.</p>
</div>
""",
 "free": True},
        {"id": 6,
 "title": "Writing Functions & Modular Code",
 "description": "Reusable R functions",
 "content": """
<div style="background-color:#002b36; color:#e0f7fa; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Writing Functions & Modular Code</h4>
  <p><strong>Functions</strong> are reusable pieces of code that perform specific tasks. 
     Instead of writing the same instructions over and over, you can wrap them in a function 
     and call it whenever needed. This makes your work faster, cleaner, and easier to share.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Functions save time and reduce errors. 
     They make your code modular, meaning you can break big problems into smaller, manageable parts. 
     Modular code is easier to read, test, and maintain — especially when projects grow larger.</p>

  <h5 class="fw-bold mt-4">Basic Function Structure</h5>
  <p>A function in R has three main parts:</p>
  <ul>
    <li><strong>Name:</strong> What you call the function.</li>
    <li><strong>Arguments:</strong> Inputs the function needs to work.</li>
    <li><strong>Body:</strong> The instructions the function runs.</li>
  </ul>
  <p>Example:</p>
  <pre><code>add_numbers <- function(x, y) {
  result <- x + y
  return(result)
}</code></pre>
  <p>Calling <code>add_numbers(3, 5)</code> will return <code>8</code>.</p>

  <h5 class="fw-bold mt-4">Modular Coding Practices</h5>
  <ul>
    <li><strong>Break tasks into smaller functions:</strong> Each function should do one job well.</li>
    <li><strong>Use clear names:</strong> Names like <code>calculate_average()</code> are easier to understand than <code>fun1()</code>.</li>
    <li><strong>Keep functions short:</strong> Long functions are harder to debug and reuse.</li>
    <li><strong>Document with comments:</strong> Explain what the function does and how to use it.</li>
    <li><strong>Test functions separately:</strong> Make sure each piece works before combining them.</li>
  </ul>

  <h5 class="fw-bold mt-4">Step-by-Step Example</h5>
  <p>Imagine you want to calculate the grade of a student based on their score:</p>
  <pre><code>calculate_grade <- function(score) {
  if(score >= 90) {
    return("A")
  } else if(score >= 75) {
    return("B")
  } else if(score >= 60) {
    return("C")
  } else {
    return("D")
  }
}</code></pre>
  <p>Now you can call <code>calculate_grade(82)</code> and get <code>"B"</code>. 
     This function is reusable for any student score.</p>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Business:</strong> Write a function to calculate monthly profit from sales and expenses.</li>
    <li><strong>Education:</strong> Automate grading by writing a function that assigns letter grades.</li>
    <li><strong>Healthcare:</strong> Create a function to calculate Body Mass Index (BMI).</li>
    <li><strong>Research:</strong> Build functions to clean survey data consistently across projects.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Start with simple functions — even adding two numbers is a good practice.</li>
    <li>Reuse functions across projects to save time.</li>
    <li>Think of functions as building blocks — combine them to solve bigger problems.</li>
    <li>Keep your code modular so others can understand and use it easily.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Functions and modular code make R programming efficient and organized. 
     By writing reusable functions, you reduce repetition and improve clarity. 
     Modular coding ensures that projects remain manageable, scalable, and easy to share.</p>

  <p class="fst-italic mt-4">In short, functions are like tools in a toolbox — 
     each one solves a specific problem, and together they build powerful solutions.</p>
</div>
""",
 "free": False},
        {"id": 7,
 "title": "Control Structures & Iteration",
 "description": "Loops and conditionals",
 "content": """
<div style="background-color:#002b36; color:#e0f7fa; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Control Structures & Iteration</h4>
  <p><strong>Control structures</strong> are the decision‑making tools in R. 
     They allow your code to choose different paths depending on conditions. 
     <strong>Iteration</strong> means repeating tasks automatically, so you don’t have to write the same code many times. 
     Together, they make your programs smarter and more efficient.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Without control structures, programs would run the same way every time. 
     With them, your code can adapt to different situations. 
     Iteration saves time by automating repetitive tasks. 
     These skills are essential for building flexible and powerful scripts.</p>

  <h5 class="fw-bold mt-4">Key Control Structures</h5>
  <ul>
    <li><strong>if/else:</strong> Decide what to do based on a condition. 
        Example: <code>if(score >= 50) { "Pass" } else { "Fail" }</code>.</li>
    <li><strong>for loop:</strong> Repeat a task a set number of times. 
        Example: <code>for(i in 1:5) { print(i) }</code> prints numbers 1 to 5.</li>
    <li><strong>while loop:</strong> Keep repeating as long as a condition is true. 
        Example: <code>while(x < 10) { x <- x + 1 }</code>.</li>
  </ul>

  <h5 class="fw-bold mt-4">Step-by-Step Example</h5>
  <p>Imagine you want to grade a list of student scores:</p>
  <pre><code>scores <- c(45, 67, 82, 90)

for(s in scores) {
  if(s >= 50) {
    print("Pass")
  } else {
    print("Fail")
  }
}</code></pre>
  <p>This loop checks each score and prints “Pass” or “Fail” automatically.</p>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Business:</strong> Use loops to calculate monthly profits for each branch.</li>
    <li><strong>Education:</strong> Apply if/else to assign grades based on exam scores.</li>
    <li><strong>Healthcare:</strong> Iterate through patient records to flag abnormal test results.</li>
    <li><strong>Research:</strong> Automate repetitive calculations across multiple datasets.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Use <code>if/else</code> for decisions, and loops for repetition.</li>
    <li>Start small — test loops with simple print statements before using them on big datasets.</li>
    <li>Be careful with <code>while</code> loops — if the condition never becomes false, the loop runs forever.</li>
    <li>Combine control structures with functions for clean, modular code.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Control structures let your code make decisions, 
     and iteration lets it repeat tasks automatically. 
     Together, they make R scripts dynamic, efficient, and adaptable to real‑world problems.</p>

  <p class="fst-italic mt-4">In short, control structures are the brain of your program, 
     and iteration is the muscle that does the work.</p>
</div>
""",
 "free": False},
        {"id": 8,
 "title": "Statistical Analysis in R",
 "description": "Basic statistical tests",
 "content": """
<div style="background-color:#002b36; color:#e0f7fa; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Statistical Analysis in R</h4>
  <p><strong>Statistical analysis</strong> is about using data to answer questions and test ideas. 
     In R, you can perform common tests like t‑tests, chi‑square tests, and correlation analysis 
     to check relationships, compare groups, and draw conclusions from datasets.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Statistics helps us move beyond guesses. 
     With proper tests, we can decide if differences or relationships in data are real 
     or just due to chance. This makes results more reliable and useful in everyday decision‑making.</p>

  <h5 class="fw-bold mt-4">Key Statistical Tests</h5>
  <ul>
    <li><strong>t‑Test:</strong> Compares the means of two groups. 
        Example: Do students in Class A score higher than those in Class B?</li>
    <li><strong>Chi‑Square Test:</strong> Checks if categories are related. 
        Example: Is product preference linked to gender?</li>
    <li><strong>Correlation Analysis:</strong> Measures how strongly two variables move together. 
        Example: Do study hours and exam scores rise together?</li>
  </ul>

  <h5 class="fw-bold mt-4">Step‑by‑Step in R</h5>
  <ul>
    <li><strong>t‑Test:</strong> <code>t.test(groupA, groupB)</code></li>
    <li><strong>Chi‑Square:</strong> <code>chisq.test(table)</code></li>
    <li><strong>Correlation:</strong> <code>cor(x, y)</code> or <code>cor.test(x, y)</code></li>
  </ul>
  <p>Each function returns results like test statistics, p‑values, and confidence intervals. 
     These numbers help you decide whether to accept or reject your hypothesis.</p>

  <h5 class="fw-bold mt-4">Interpreting Outputs</h5>
  <ul>
    <li><strong>p‑Value:</strong> A small p‑value (usually less than 0.05) suggests the result is statistically significant.</li>
    <li><strong>Confidence Interval:</strong> Shows the range where the true value likely lies.</li>
    <li><strong>Correlation Coefficient:</strong> Values close to +1 or ‑1 show strong relationships, while values near 0 show weak or no relationship.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Business:</strong> Test if a new advertisement increases sales compared to the old one.</li>
    <li><strong>Education:</strong> Compare exam scores between two teaching methods.</li>
    <li><strong>Healthcare:</strong> Check if a new drug improves recovery rates compared to standard treatment.</li>
    <li><strong>Research:</strong> Measure correlation between income and education level.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Always check assumptions before running tests (e.g., normal distribution for t‑tests).</li>
    <li>Don’t rely only on p‑values — look at effect sizes and confidence intervals too.</li>
    <li>Visualize data with plots before and after analysis to understand patterns.</li>
    <li>Practice with small datasets to build confidence before tackling larger ones.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Statistical analysis in R helps you test ideas and uncover patterns in data. 
     By applying t‑tests, chi‑square tests, and correlation analysis, 
     you can move from raw numbers to meaningful insights. 
     These tools make your conclusions stronger and your decisions smarter.</p>

  <p class="fst-italic mt-4">In short, statistical analysis is like a truth detector — 
     it helps you see whether patterns in data are real or just noise.</p>
</div>
""",
 "free": False},
        {"id": 9,
 "title": "Working with Dates & Strings",
 "description": "Handle date-time and text data",
 "content": """
<div style="background-color:#002b36; color:#e0f7fa; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Working with Dates & Strings</h4>
  <p>Data often includes <strong>dates</strong> (like birthdays, transaction times) and <strong>strings</strong> (text such as names or comments). 
     Handling these correctly is important because messy dates or inconsistent text can make analysis confusing. 
     R provides packages like <code>lubridate</code> for dates and <code>stringr</code> for text, 
     making it easier to parse, format, and clean this type of data.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Dates and strings appear in almost every dataset. 
     For example, businesses track sales dates, schools record student names, and researchers collect survey responses. 
     Clean and consistent handling of this data ensures accurate analysis and clear communication.</p>

  <h5 class="fw-bold mt-4">Working with Dates (lubridate)</h5>
  <ul>
    <li><strong>Parsing Dates:</strong> Convert text into proper date objects. 
        Example: <code>ymd("2025-01-15")</code> turns a string into a date.</li>
    <li><strong>Extracting Components:</strong> Get year, month, or day easily. 
        Example: <code>year(date)</code> or <code>month(date)</code>.</li>
    <li><strong>Formatting:</strong> Display dates in readable formats. 
        Example: <code>format(date, "%B %d, %Y")</code> shows “January 15, 2026”.</li>
    <li><strong>Arithmetic:</strong> Add or subtract days. 
        Example: <code>date + days(7)</code> moves a date forward by a week.</li>
  </ul>

  <h5 class="fw-bold mt-4">Working with Strings (stringr)</h5>
  <ul>
    <li><strong>Cleaning Text:</strong> Remove extra spaces with <code>str_trim()</code>.</li>
    <li><strong>Changing Case:</strong> Convert text to lower or upper case with <code>str_to_lower()</code> or <code>str_to_upper()</code>.</li>
    <li><strong>Finding Patterns:</strong> Use <code>str_detect()</code> to check if a word appears in text.</li>
    <li><strong>Replacing Text:</strong> Use <code>str_replace()</code> to fix typos or standardize words.</li>
    <li><strong>Splitting Text:</strong> Break sentences into words with <code>str_split()</code>.</li>
  </ul>

  <h5 class="fw-bold mt-4">Step-by-Step Example</h5>
  <p>Imagine you have a dataset of customer names and purchase dates:</p>
  <ol>
    <li>Use <code>ymd()</code> to convert purchase dates from text into proper date objects.</li>
    <li>Extract the month with <code>month()</code> to see which month has the most purchases.</li>
    <li>Clean customer names with <code>str_trim()</code> to remove extra spaces.</li>
    <li>Standardize names with <code>str_to_title()</code> so “john doe” becomes “John Doe”.</li>
  </ol>
  <p>This workflow ensures both dates and names are clean and ready for analysis.</p>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Business:</strong> Track sales by month using cleaned date fields.</li>
    <li><strong>Education:</strong> Standardize student names for consistent reporting.</li>
    <li><strong>Healthcare:</strong> Calculate patient age from birth dates.</li>
    <li><strong>Research:</strong> Clean survey responses by fixing inconsistent text entries.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Always convert dates into proper date objects before analysis.</li>
    <li>Use string functions to clean messy text — consistency is key.</li>
    <li>Practice with small datasets to build confidence.</li>
    <li>Combine date and string functions for powerful data cleaning workflows.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Dates and strings are everywhere in data. 
     By using <code>lubridate</code> and <code>stringr</code>, 
     you can parse, clean, and format them easily. 
     This makes your datasets more reliable and your analysis more meaningful.</p>

  <p class="fst-italic mt-4">In short, dates tell you “when,” and strings tell you “what” — 
     mastering both makes your data analysis complete.</p>
</div>
""",
 "free": False},
        {"id": 10,
 "title": "Data Reshaping with tidyr",
 "description": "Tidy data principles",
 "content": """
<div style="background-color:#002b36; color:#e0f7fa; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Data Reshaping with tidyr</h4>
  <p><strong>Tidy data</strong> means organizing datasets so that each column is a variable, 
     each row is an observation, and each cell contains a single value. 
     The <code>tidyr</code> package in R helps you reshape messy datasets into tidy formats, 
     making them easier to analyze and visualize.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Messy data is hard to work with. 
     Sometimes values are spread across multiple columns, or one column contains too much information. 
     Reshaping data ensures consistency, clarity, and makes analysis smoother. 
     Tidy data is the foundation of reproducible and reliable results.</p>

  <h5 class="fw-bold mt-4">Key tidyr Functions</h5>
  <ul>
    <li><strong>pivot_longer():</strong> Turns wide data into long format. 
        Example: Convert exam scores stored in separate columns (Math, English, Science) 
        into one column called “Subject” with another column for “Score.”</li>
    <li><strong>pivot_wider():</strong> Turns long data into wide format. 
        Example: Spread survey responses so each question becomes its own column.</li>
    <li><strong>separate():</strong> Splits one column into multiple parts. 
        Example: Break “2026-01-15” into “Year,” “Month,” and “Day.”</li>
    <li><strong>unite():</strong> Combines multiple columns into one. 
        Example: Merge “First Name” and “Last Name” into a single “Full Name” column.</li>
  </ul>

  <h5 class="fw-bold mt-4">Step-by-Step Example</h5>
  <p>Imagine you have a dataset of student scores:</p>
  <ol>
    <li>Use <code>pivot_longer()</code> to gather subject scores into one column.</li>
    <li>Use <code>separate()</code> to split a “Date” column into year, month, and day.</li>
    <li>Use <code>unite()</code> to combine “First Name” and “Last Name.”</li>
    <li>Finally, use <code>pivot_wider()</code> if you want to spread results back into columns.</li>
  </ol>
  <p>This workflow transforms messy tables into tidy datasets ready for analysis.</p>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Business:</strong> Reshape sales data so each product and month is clearly represented.</li>
    <li><strong>Education:</strong> Organize exam scores across subjects into tidy formats for comparison.</li>
    <li><strong>Healthcare:</strong> Split patient records into separate columns for date, time, and diagnosis.</li>
    <li><strong>Research:</strong> Combine multiple survey fields into one clean dataset for analysis.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Think of tidy data as “one variable per column, one observation per row.”</li>
    <li>Use <code>pivot_longer()</code> when data feels too spread out.</li>
    <li>Use <code>pivot_wider()</code> when data feels too stacked.</li>
    <li>Practice with small datasets before reshaping large ones.</li>
    <li>Combine tidyr with dplyr for powerful data cleaning workflows.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Reshaping data with tidyr makes messy datasets tidy and analysis‑ready. 
     By mastering functions like <code>pivot_longer()</code>, <code>pivot_wider()</code>, <code>separate()</code>, and <code>unite()</code>, 
     you can transform complex tables into clear, structured formats. 
     Tidy data principles ensure that your work is consistent, reproducible, and easy to share.</p>

  <p class="fst-italic mt-4">In short, tidyr is like an organizer’s toolkit — 
     it reshapes messy tables into neat, tidy datasets that tell a clear story.</p>
</div>
""",
 "free": False},
        {"id": 11,
 "title": "Advanced Visualization Techniques",
 "description": "Interactive plots",
 "content": """
<div style="background-color:#002b36; color:#e0f7fa; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Advanced Visualization Techniques</h4>
  <p>Once you master basic charts with ggplot2, you can move into <strong>advanced visualization</strong>. 
     This means creating interactive plots and dashboards that allow users to explore data in real time. 
     Libraries like <code>plotly</code> and <code>highcharter</code> make it possible to add interactivity, 
     hover effects, zooming, and clickable elements to your charts.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Interactive visualizations go beyond static charts. 
     They let users dig deeper into the data, highlight specific points, and discover insights on their own. 
     Businesses use dashboards to monitor performance, educators use interactive plots to teach concepts, 
     and researchers use them to share findings in a more engaging way.</p>

  <h5 class="fw-bold mt-4">Key Libraries</h5>
  <ul>
    <li><strong>plotly:</strong> Adds interactivity to ggplot2 charts or creates new ones directly. 
        Example: Hovering over a point shows its exact value.</li>
    <li><strong>highcharter:</strong> Based on Highcharts, it offers polished, interactive charts with themes and tooltips.</li>
    <li><strong>shiny:</strong> Used to build interactive dashboards that combine multiple plots, tables, and inputs.</li>
  </ul>

  <h5 class="fw-bold mt-4">Step-by-Step Example</h5>
  <p>Imagine you have a dataset of monthly sales:</p>
  <ol>
    <li>Create a line chart with ggplot2 showing sales over time.</li>
    <li>Convert it to an interactive plot with <code>ggplotly()</code> from plotly.</li>
    <li>Add hover tooltips so users can see exact sales values for each month.</li>
    <li>Embed the chart in a Shiny dashboard with filters for region or product type.</li>
  </ol>
  <p>This workflow turns a simple chart into a dynamic tool for exploring business performance.</p>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Business:</strong> Interactive dashboards track sales, expenses, and customer trends in real time.</li>
    <li><strong>Education:</strong> Teachers use interactive plots to show how changing variables affect outcomes.</li>
    <li><strong>Healthcare:</strong> Doctors visualize patient data interactively to monitor progress.</li>
    <li><strong>Research:</strong> Scientists share interactive charts so others can explore experimental results.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Start with ggplot2 charts, then add interactivity using <code>plotly</code>.</li>
    <li>Use tooltips and hover effects to make charts more informative.</li>
    <li>Keep dashboards simple — too many charts can overwhelm users.</li>
    <li>Focus on clarity: interactive features should enhance, not distract.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Advanced visualization techniques bring your data to life. 
     By using libraries like plotly, highcharter, and shiny, 
     you can create interactive plots and dashboards that make analysis engaging and insightful. 
     These tools transform charts from static pictures into dynamic experiences.</p>

  <p class="fst-italic mt-4">In short, advanced visualization is like moving from a photo to a video — 
     it lets users explore data in motion.</p>
</div>
""",
 "free": False},
        {"id": 12,
 "title": "Introduction to Shiny Apps",
 "description": "Build web apps with R",
 "content": """
<div style="background-color:#002b36; color:#e0f7fa; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Introduction to Shiny Apps</h4>
  <p><strong>Shiny</strong> is an R package that makes it easy to build interactive web applications directly from R. 
     With Shiny, you can turn your analyses into apps that others can use without writing extra code in HTML, CSS, or JavaScript. 
     It combines <strong>UI components</strong> (what users see) and <strong>server logic</strong> (what R does behind the scenes) 
     to create dynamic dashboards and tools.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Shiny apps allow you to share your work interactively. 
     Instead of sending static reports, you can give users a live app where they can filter data, 
     change inputs, and see updated results instantly. 
     Businesses use Shiny for dashboards, educators use it for teaching, and researchers use it to share findings.</p>

  <h5 class="fw-bold mt-4">Basic Structure of a Shiny App</h5>
  <ul>
    <li><strong>UI (User Interface):</strong> Defines the layout and components users interact with, such as buttons, sliders, and plots.</li>
    <li><strong>Server:</strong> Contains the R code that processes inputs and generates outputs.</li>
    <li><strong>shinyApp():</strong> Combines the UI and server into a working app.</li>
  </ul>

  <h5 class="fw-bold mt-4">Step-by-Step Example</h5>
  <p>Here’s a simple Shiny app that displays a histogram:</p>
  <pre><code>library(shiny)

ui <- fluidPage(
  titlePanel("Histogram Example"),
  sidebarLayout(
    sidebarPanel(
      sliderInput("bins", "Number of bins:", min = 5, max = 50, value = 20)
    ),
    mainPanel(
      plotOutput("distPlot")
    )
  )
)

server <- function(input, output) {
  output$distPlot <- renderPlot({
    hist(rnorm(500), breaks = input$bins, col = "skyblue", border = "white")
  })
}

shinyApp(ui = ui, server = server)</code></pre>
  <p>This app lets users adjust the number of bins in the histogram with a slider, 
     and the plot updates instantly.</p>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Business:</strong> Build dashboards to track sales and performance metrics.</li>
    <li><strong>Education:</strong> Create interactive tools for students to explore statistical concepts.</li>
    <li><strong>Healthcare:</strong> Develop apps to visualize patient data and monitor health trends.</li>
    <li><strong>Research:</strong> Share interactive models and simulations with collaborators.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Start small — build simple apps before moving to complex dashboards.</li>
    <li>Use built‑in UI functions like <code>sliderInput()</code> and <code>selectInput()</code> to add interactivity quickly.</li>
    <li>Keep the design clean and intuitive — users should focus on the data, not struggle with navigation.</li>
    <li>Test your app often to make sure inputs and outputs work as expected.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Shiny apps transform R analyses into interactive experiences. 
     By combining UI components with server logic, you can build tools that let users explore data in real time. 
     This makes your work more engaging, accessible, and impactful.</p>

  <p class="fst-italic mt-4">In short, Shiny is like giving your analysis a “control panel” — 
     users can push buttons, move sliders, and see results instantly.</p>
</div>
""",
 "free": False},
        {"id": 13,
 "title": "R Markdown for Reporting",
 "description": "Dynamic documents",
 "content": """
<div style="background-color:#002b36; color:#e0f7fa; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">R Markdown for Reporting</h4>
  <p><strong>R Markdown</strong> is a tool that lets you combine code, results, and explanations in one document. 
     Instead of keeping your analysis separate from your report, R Markdown integrates everything — 
     making your work reproducible, clear, and easy to share.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Reports are more powerful when they show both the process and the results. 
     With R Markdown, you can write text, run R code, and display outputs (like tables and plots) 
     all in the same file. This ensures that anyone reading your report can see exactly how the results were produced.</p>

  <h5 class="fw-bold mt-4">Basic Structure</h5>
  <ul>
    <li><strong>YAML Header:</strong> At the top of the file, you define the title, author, and output format (HTML, PDF, Word).</li>
    <li><strong>Text Sections:</strong> Written in Markdown, using simple formatting like <code># Headings</code>, <code>**bold**</code>, or <code>*italics*</code>.</li>
    <li><strong>Code Chunks:</strong> Written inside triple backticks (<code>```{r}</code>), where R code is executed and results are shown.</li>
    <li><strong>Outputs:</strong> Tables, plots, and summaries appear directly in the report after the code runs.</li>
  </ul>

  <h5 class="fw-bold mt-4">Step-by-Step Example</h5>
  <p>Here’s a simple R Markdown workflow:</p>
  <ol>
    <li>Start with a YAML header:
      <pre><code>---
title: "My Report"
author: "Evanson"
output: html_document
---</code></pre></li>
    <li>Write narrative text to explain your analysis.</li>
    <li>Add a code chunk:
      <pre><code>```{r}
summary(cars)
```</code></pre></li>
    <li>Knit the document to produce an HTML report with text and results together.</li>
  </ol>

  <h5 class="fw-bold mt-4">Export Options</h5>
  <ul>
    <li><strong>HTML:</strong> Interactive reports viewable in a browser.</li>
    <li><strong>PDF:</strong> Professional reports for printing or sharing.</li>
    <li><strong>Word:</strong> Editable documents for collaboration.</li>
  </ul>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Business:</strong> Create dynamic sales reports that update automatically when new data is added.</li>
    <li><strong>Education:</strong> Teachers prepare reproducible lecture notes with code and explanations.</li>
    <li><strong>Healthcare:</strong> Generate patient data summaries with charts and statistics in one document.</li>
    <li><strong>Research:</strong> Publish reproducible papers where readers can see both the analysis and the narrative.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Start with HTML output — it’s the easiest to use and view.</li>
    <li>Use headings and lists to organize your report clearly.</li>
    <li>Keep code chunks small and focused on one task.</li>
    <li>Practice knitting often to check how your report looks.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>R Markdown makes reporting dynamic and reproducible. 
     By combining text, code, and outputs in one place, 
     you create documents that are transparent, professional, and easy to share. 
     This approach ensures that your analysis can be trusted and understood by others.</p>

  <p class="fst-italic mt-4">In short, R Markdown is like a notebook that writes itself — 
     blending code, results, and explanations into one seamless report.</p>
</div>
""",
 "free": False},
        {"id": 14,
 "title": "Package Development Basics",
 "description": "Create R packages",
 "content": """
<div style="background-color:#002b36; color:#e0f7fa; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Package Development Basics</h4>
  <p><strong>R packages</strong> are collections of functions, data, and documentation bundled together. 
     They make it easy to share reusable code with others and keep projects organized. 
     Learning how to build packages helps you move from writing scripts for yourself 
     to creating tools that others can use.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Packages allow you to distribute your work in a professional way. 
     Instead of copying and pasting code across projects, you can store functions in a package 
     and load them with a single command. This improves reproducibility, saves time, 
     and makes collaboration smoother.</p>

  <h5 class="fw-bold mt-4">Basic Structure of an R Package</h5>
  <ul>
    <li><strong>DESCRIPTION file:</strong> Contains metadata like package name, version, author, and dependencies.</li>
    <li><strong>NAMESPACE file:</strong> Controls which functions are available to users.</li>
    <li><strong>R/ folder:</strong> Stores the actual R functions.</li>
    <li><strong>man/ folder:</strong> Holds documentation for each function.</li>
    <li><strong>data/ folder:</strong> Optional — includes datasets packaged with your code.</li>
    <li><strong>tests/ folder:</strong> Optional — contains unit tests to check that functions work correctly.</li>
  </ul>

  <h5 class="fw-bold mt-4">Step-by-Step Example</h5>
  <p>Here’s a simple workflow to create a package:</p>
  <ol>
    <li>Use <code>usethis::create_package("mypackage")</code> to set up the structure.</li>
    <li>Add functions in the <code>R/</code> folder, e.g., <code>hello_world()</code>.</li>
    <li>Document functions with <code>roxygen2</code> comments (starting with <code>#'</code>).</li>
    <li>Run <code>devtools::document()</code> to generate help files in the <code>man/</code> folder.</li>
    <li>Build and install the package with <code>devtools::install()</code>.</li>
    <li>Load your package with <code>library(mypackage)</code> and use your functions.</li>
  </ol>

  <h5 class="fw-bold mt-4">Documenting Functions</h5>
  <p>Good documentation makes packages easy to use. 
     With <code>roxygen2</code>, you can write comments above each function that describe what it does, 
     its inputs, and outputs. These comments are automatically turned into help pages.</p>
  <pre><code>#' Add two numbers
#'
#' @param x First number
#' @param y Second number
#' @return Sum of x and y
#' @examples
#' add_numbers(2, 3)
add_numbers <- function(x, y) {
  x + y
}</code></pre>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Business:</strong> Package reusable functions for sales forecasting.</li>
    <li><strong>Education:</strong> Create teaching tools with custom functions for students.</li>
    <li><strong>Healthcare:</strong> Bundle analysis functions for patient data monitoring.</li>
    <li><strong>Research:</strong> Share statistical models and cleaning functions with collaborators.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Start small — even one function can be packaged.</li>
    <li>Use <code>usethis</code> and <code>devtools</code> to simplify setup and testing.</li>
    <li>Write clear documentation so others understand your work.</li>
    <li>Test your functions before sharing the package.</li>
    <li>Keep improving — packages can grow as your skills and needs expand.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>Package development turns your code into reusable tools. 
     By learning the structure, documenting functions, and sharing packages, 
     you make your work more professional, reproducible, and impactful. 
     Packages are the bridge between personal scripts and community‑ready solutions.</p>

  <p class="fst-italic mt-4">In short, packages are like gift boxes — 
     they wrap your code neatly so others can use it easily.</p>
</div>
""",
 "free": False},
        {"id": 15,
 "title": "Capstone Project: R Analysis",
 "description": "Complete data analysis project in R",
 "content": """
<div style="background-color:#002b36; color:#e0f7fa; padding:1.5rem; border-radius:10px;">
  <h4 class="fw-bold">Capstone Project: R Analysis</h4>
  <p>The capstone project is your chance to bring together everything you’ve learned in R. 
     You will apply skills in cleaning, manipulation, visualization, and statistical analysis 
     to a real dataset, then present your findings in a final report. 
     This project shows how all the pieces fit together in a complete workflow.</p>

  <h5 class="fw-bold mt-4">Why It Matters</h5>
  <p>Working on a full project helps you practice the entire data science process. 
     It’s not just about writing code — it’s about asking questions, preparing data, 
     analyzing results, and communicating insights clearly. 
     This is the kind of work you’ll do in real jobs and research projects.</p>

  <h5 class="fw-bold mt-4">Step-by-Step Workflow</h5>
  <ol>
    <li><strong>Choose a Dataset:</strong> Pick a dataset that interests you (e.g., sales records, exam scores, health data).</li>
    <li><strong>Import Data:</strong> Load the dataset into R using <code>read.csv()</code>, <code>read_excel()</code>, or other functions.</li>
    <li><strong>Clean Data:</strong> Handle missing values, remove duplicates, and fix inconsistent formats.</li>
    <li><strong>Manipulate Data:</strong> Use <code>dplyr</code> functions like <code>filter()</code>, <code>mutate()</code>, and <code>group_by()</code> to prepare the dataset.</li>
    <li><strong>Visualize Data:</strong> Create charts with <code>ggplot2</code> to explore patterns and trends.</li>
    <li><strong>Statistical Analysis:</strong> Apply tests such as t‑tests, chi‑square, or correlation to answer specific questions.</li>
    <li><strong>Final Report:</strong> Use R Markdown to combine code, outputs, and explanations into a polished document.</li>
  </ol>

  <h5 class="fw-bold mt-4">Everyday Examples</h5>
  <ul>
    <li><strong>Business:</strong> Analyze sales data to find which products perform best and present results in a dashboard.</li>
    <li><strong>Education:</strong> Study exam scores to compare performance across different classes or teaching methods.</li>
    <li><strong>Healthcare:</strong> Explore patient records to identify trends in recovery times or treatment outcomes.</li>
    <li><strong>Research:</strong> Clean and analyze survey data to uncover meaningful insights about behavior or opinions.</li>
  </ul>

  <h5 class="fw-bold mt-4">Tips for Beginners</h5>
  <ul>
    <li>Pick a dataset that excites you — motivation makes the project easier.</li>
    <li>Break the project into small steps instead of trying to do everything at once.</li>
    <li>Document your process so others can follow your work.</li>
    <li>Focus on clarity in your final report — simple visuals and explanations are more effective than complex ones.</li>
  </ul>

  <h5 class="fw-bold mt-4">The Big Idea</h5>
  <p>The capstone project is about applying all your R skills in one place. 
     By cleaning, manipulating, visualizing, and analyzing a dataset, 
     you’ll create a complete report that demonstrates your ability to handle real‑world data. 
     This project is the bridge between learning R and using it professionally.</p>

  <p class="fst-italic mt-4">In short, the capstone is your showcase — 
     proof that you can take raw data and turn it into meaningful insights.</p>
</div>
""",
 "free": False},
    ]
}
}
