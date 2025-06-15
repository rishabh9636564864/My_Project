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
#--> Save changes
conn.commit()

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
##--> Read Data from SQL Table into Pandas <--##
#-> Query the data from the database
df = pd.read_sql_query("SELECT * FROM students", conn)
print(df)

##--> Perform Some Analysis <--##
#-> Calculate Average Score
avg_score = df['score'].mean()
print(f"\n* Average score: {avg_score}")

#--> Group by parent education and find average scores
group = df.groupby('parent_education')['score'].mean()
print("\n* Average Score by Parent Education:")
print(group)

##--> Data Visualization<--##
#-> Plotting scores based on hours studied
sns.scatterplot(data=df,x='hours_studied', y='score', hue='gender')
plt.title('Hours Studied vs Score')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.grid(True)
plt.show()
