import pandas as pd    
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("student_scores.csv")

#--> Basic data overview <--#
print("* First 5 rows of the dataset:")
print(df.head())
print("\n* Dataset Info:")
print(df.info())
print("\n* Summary Statistics:")
print(df.describe())
print("\n* Gender Counts:")
print(df['Gender'].value_counts())

#--> Visualization <--#
#1 Score distribution
plt.figure(figsize=(6,4))
sns.histplot(df['Score'], kde=True)
plt.title('Distribution of Scores')
plt.show()

#2 Hours vs Score
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x='Hours_Studied', y='Score', hue='Gender')
plt.title('Hours Studied vs Score')
plt.show()

#3 Boxplot by Gender
sns.boxplot(data=df, x='Gender', y='Score')
plt.title('Scores by Gender')
plt.show()

#--> Correlation Analysis <--#
print(df[['Hours_Studied', 'Score']].corr())

#--> Group Analysis <--#
grouped = df.groupby('Parent_Education')['Score'].mean()
print(grouped)