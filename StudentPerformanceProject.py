#--> Importing required libraries
import sqlite3   # To create and interact with the SQLite database
import pandas as pd  # To load and analyze data
import matplotlib.pyplot as plt # for data visualization
import seaborn as sns           # for data visualization

#--> Create a connection to a new SQLite database file
conn = sqlite3.connect("students.db")  # This creates a new database file named 'students.db'

#--> Create a cursor object to execute SQL commands
cursor = conn.cursor()
"""
#--> Create a table called 'students'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        gender TEXT,
        hours_studied INTEGER,
        parent_education TEXT,
        score INTEGER
    )
''')
"""
#--> Creating the 'subjects' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        subject_id INTEGER PRIMARY KEY,
        subject_name TEXT
    )
''')

#--> Creating the 'scores' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        score INTEGER,
        FOREIGN KEY(student_id) REFERENCES students(id),
        FOREIGN KEY(subject_id) REFERENCES subjects(subject_id)
    )
''')

#--> Save changes
conn.commit()

"""
#-> Sample data to insert
student_data = [
    (1, 'Aliya', 'Female', 4, 'Bachelor', 78),
    (2, 'Bhaskar', 'Male', 2, 'High School', 50),
    (3, 'Charit', 'Male', 5, 'Master', 88),
    (4, 'Dherya', 'Female', 3, 'Bachelor', 65),
    (5, 'Eshan', 'Male', 1, 'High School', 40)
]

#-> Insert data into the 'students' table
cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?)", student_data)
#-> Save changes
conn.commit()
"""
#--> Insert sample subjects
subjects = [
    (1, 'Math'),
    (2, 'Science'),
    (3, 'English')
]

cursor.executemany("INSERT OR IGNORE INTO subjects VALUES (?, ?)", subjects)
conn.commit()

#--> Sample scores: (id, student_id, subject_id, score)
scores = [
    (1, 1, 1, 85),  # Aliya - Math
    (2, 1, 2, 78),  # Aliya - Science
    (3, 1, 3, 88),  # Aliya - English

    (4, 2, 1, 45),  # Bhaskar - Math
    (5, 2, 2, 55),  # Bhaskar - Science
    (6, 2, 3, 50),  # Bhaskar - English

    (7, 3, 1, 92),  # Charit - Math
    (8, 3, 2, 85),  # Charit - Science
    (9, 3, 3, 88),  # Charit - English

    (10, 4, 1, 76),  # Dherya - Math
    (11, 4, 2, 65),  # Dherya - Science
    (12, 4, 3, 71),  # Dherya - English

    (13, 5, 1, 90),  # Eshan - Math
    (14, 5, 2, 55),  # Eshan - Science
    (15, 5, 3, 57),  # Eshan - English
]

cursor.executemany("INSERT OR IGNORE INTO scores VALUES (?, ?, ?, ?)", scores)
conn.commit()

##--> Read Data from SQL Table into Pandas <--##
#-> Query the data from the database
df = pd.read_sql_query("SELECT * FROM students", conn)
print("\n==> Student Table <==")
print(df)

df = pd.read_sql_query("SELECT * FROM subjects", conn)
print("\n==> Subject Table <==")
print(df)

df = pd.read_sql_query("SELECT * FROM scores", conn)
print("\n==> Score Table <==")
print(df)

#--> Query: Join students, scores, subjects
query = '''
SELECT 
    students.name AS student_name,
    subjects.subject_name,
    scores.score
FROM scores
JOIN students ON scores.student_id = students.id
JOIN subjects ON scores.subject_id = subjects.subject_id
ORDER BY students.name
'''

#-> Load into DataFrame
df_scores = pd.read_sql_query(query, conn)
print("\n#==> Each Student's Scores <==#")
print(df_scores)

##--> Perform Some Analysis <--##
#-> Calculate Average Score
avg_score = df['score'].mean()
print(f"\n* Average score: {avg_score}")

"""
#--> Group by parent education and find average scores
group = df.groupby('parent_education')['score'].mean()
print("\n* Average Score by Parent Education:")
print(group)
"""
#--> Find Average Score Per Subject
query_avg_subject = '''
SELECT 
    subjects.subject_name,
    AVG(scores.score) AS average_score
FROM scores
JOIN subjects ON scores.subject_id = subjects.subject_id
GROUP BY subjects.subject_name
ORDER BY average_score DESC
'''
df_avg = pd.read_sql_query(query_avg_subject, conn)
print("\n* Average Score by Subject:")
print(df_avg)

#--> Filter: Students Who Scored > 80 in Math
query_top_math = '''
SELECT 
    students.name AS student_name,
    scores.score
FROM scores
JOIN students ON scores.student_id = students.id
WHERE scores.subject_id = 1 AND scores.score > 80
'''

df_math_top = pd.read_sql_query(query_top_math, conn)
print("\n* Students Who Scored > 80 in Math:")
print(df_math_top)

"""
##--> Data Visualization<--##
#-> Plotting scores based on hours studied
sns.scatterplot(data=df,x='hours_studied', y='score', hue='gender')
plt.title('Hours Studied vs Score')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.grid(True)
plt.show()
"""
#--> Visualize Scores per Subject
plt.figure(figsize=(8,5))
sns.barplot(data=df_scores, x='subject_name', y='score', hue='student_name')
plt.title('Scores per Subject by Student')
plt.xlabel('Subject')
plt.ylabel('Score')
plt.tight_layout()
plt.show()