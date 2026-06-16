#NumPy
import numpy as np
 
# # Create arrays
# arr1d = np.array([1, 2, 3, 4, 5])
# arr2d = np.array([[85,90,78],[72,88,95],[91,76,83]])  # 3 students x 3 subjects
 
# print(arr2d.shape)     # (3, 3)
# print(arr2d.dtype)     # int64
# print(arr2d.ndim)      # 2 (2-dimensional)

# zeros = np.zeros((3,4))           		# 3x4 array of 0s
# ones  = np.ones((2,5))            		# 2x5 array of 1s
# rng   = np.arange(0,50,5)         		# [0,5,10,15,...,45]
# lin   = np.linspace(0,1,11)       		# 11 evenly spaced from 0 to 1
# rand  = np.random.randint(40,100,(5,3))

# print("zeros:", zeros)
# print("ones:", ones)
# print("rng:", rng)
# print("lin:", lin)
# print("rand:", rand)

# # Vectorised math — no loops needed!
# arr = np.array([10,20,30,40,50])
# print(arr * 2)        # [20 40 60 80 100]
# print(arr + 5)        # [15 25 35 45 55]
# print(arr ** 2)       # [100 400 900 1600 2500]

# # Statistics on arrays
# marks_2d = np.array([[85,90,78],[72,88,95],[91,76,83]])
# print(np.mean(marks_2d))           # Overall mean
# print(np.mean(marks_2d, axis=1))   # Mean per student (row)
# print(np.mean(marks_2d, axis=0))   # Mean per subject (column)
# print(np.max(marks_2d))            # Highest mark
# print(np.std(marks_2d))            # Standard deviation
 
# # Boolean indexing (critical for data filtering!)
# arr = np.array([55,82,43,91,67,78,35,88])
# print(arr[arr > 70])   # [82 91 78 88] — only values > 70

# import csv

# records = [
#     ['Name','Marks','City','Grade'],
#     ['Rahul',85,'Bhopal','B'],
#     ['Priya',92,'Indore','A'],
#     ['Amit',73,'Jabalpur','B'],
# ]
# with open('students.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)



import pandas as pd
 
# Create DataFrame from dictionary
data = {
    'Name':   ['Rahul','Priya','Amit','Sneha','Vikram'],
    'Age':    [22, 21, 23, 20, 24],
    'Marks':  [85, 92, 78, 88, 73],
    'City':   ['Bhopal','Indore','Bhopal','Jabalpur','Indore'],
}
df = pd.DataFrame(data)
 
# Explore the data
# print(df.shape)          # (5, 4) — 5 rows, 4 columns
# print(df.head(3))        # First 3 rows
# print(df.dtypes)         # Data type of each column
# print(df.describe())     # Statistical summary
 
# Select columns
# print(df['Name'])                   # Single column → Series
# print(df[['Name', 'Marks']])        # Multiple → DataFrame
 
# Filter rows
# print(df[df['Marks'] >= 85])        # High scorers
# print(df[df['City'] == 'Bhopal'])   # Bhopal students
# print(df[(df['Marks']>=80) & (df['City']=='Indore')])  # Multiple conditions
 
# Add computed column
# def get_grade(x):
#     if x >= 90:
#         return 'A'
#     elif x >= 75:
#         return 'B'
#     else:
#         return 'C'

# df['Grade'] = df['Marks'].apply(get_grade)
# print(df['Grade'])
 
# # GroupBy — like Excel pivot
# city_avg = df.groupby('City')['Marks'].mean()
# print(city_avg)
 
# # Read real CSV file
# df2 = pd.read_csv('students.csv')
# df2.to_csv('clean_output.csv', index=False)  # Save

import matplotlib.pyplot as plt
import numpy as np
 
# Data
# months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# sales  = [45,52,48,61,58,72,69,75,68,82,90,95]  # in thousands

# LINE CHART — trends over time 
# plt.figure(figsize=(12,5))
# plt.plot(months, sales, marker='o', color='steelblue', linewidth=2, markersize=8)
# plt.fill_between(months, sales, alpha=0.15, color='steelblue')
# plt.title('Monthly Sales 2024 (Rs. Thousands)', fontsize=14, fontweight='bold')
# plt.xlabel('Month')
# plt.ylabel('Sales (Rs. K)')
# plt.grid(True, alpha=0.3)
# plt.tight_layout()
# plt.show()
 
# BAR CHART — comparing categories
# cities = ['Bhopal','Indore','Jabalpur','Gwalior','Ujjain']
# students = [1200, 2800, 980, 850, 650]
# colors = ['#2196F3','#4CAF50','#FF9800','#9C27B0','#F44336']
 
# plt.figure(figsize=(9,5))
# bars = plt.bar(cities, students, color=colors, edgecolor='white',linewidth=1.5)
# plt.title('Students Enrolled per City')
# plt.ylabel('Number of Students')
# for bar,val in zip(bars,students):
#     plt.text(bar.get_x()+bar.get_width()/2, val+30, str(val), ha='center',fontweight='bold')
# # plt.tight_layout()
# plt.show()
 
# # SCATTER PLOT — relationship between two variables
# study_hrs = np.random.uniform(2,10,50)
# print(study_hrs)
# marks = study_hrs * 7 + np.random.normal(0,8,50)
# print(marks)
# marks = np.clip(marks, 30, 100)
# print(marks)
 
# plt.figure(figsize=(8,5))
# plt.scatter(study_hrs, marks, c=marks, cmap='RdYlGn', s=100, alpha=0.8)
# plt.colorbar(label='Marks')
# plt.title('Study Hours vs Exam Marks')
# plt.xlabel('Study Hours/Day')
# plt.ylabel('Exam Marks')
# plt.show()

# import seaborn as sns
# import pandas as pd
# import numpy as np
 
# np.random.seed(42)
# df = pd.DataFrame({
#     'marks':       np.random.randint(40,100,100),
#     'study_hours': np.random.uniform(2,10,100),
#     'city':        np.random.choice(['Bhopal','Indore','Jabalpur'],100),
#     'gender':      np.random.choice(['Male','Female'],100)
# })
 
# # Histogram with KDE — see the distribution
# plt.figure(figsize=(10,4))
# sns.histplot(df['marks'], bins=20, kde=True, color='steelblue')
# plt.title('Distribution of Student Marks')
# plt.show()
 
# # Box plot — outliers and spread per group
# sns.boxplot(data=df, x='city', y='marks', palette='Set2')
# plt.title('Marks Distribution by City'); plt.show() 

# # Correlation Heatmap — critical in data science
# plt.figure(figsize=(5,4))
# sns.heatmap(df[['marks','study_hours']].corr(),annot=True,cmap='coolwarm',vmin=-1,vmax=1)
# plt.title('Correlation Matrix'); plt.show()
 
# # Pair plot — all relationships at once
# sns.pairplot(df[['marks','study_hours']],diag_kind='kde')
# plt.show()

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy import stats
 
# # Employee salaries (in thousands Rs.)
# salaries = [22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]
 
# # Central Tendency — where is the 'centre' of data?
# mean   = np.mean(salaries)         # Average
# median = np.median(salaries)       # Middle value when sorted
# mode   = stats.mode(salaries,keepdims=True).mode[0]  # Most frequent
 
# print(f'Mean   (Average):     Rs.{mean:.1f}K')
# print(f'Median (Middle value): Rs.{median}K')
# print(f'Mode   (Most common):  Rs.{mode}K')

# # Spread — how varied is the data?
# std  = np.std(salaries)            # Standard deviation
# var  = np.var(salaries)            # Variance (std squared)
# rng  = max(salaries)-min(salaries) # Range
# q1   = np.percentile(salaries,25)  # 25th percentile
# q3   = np.percentile(salaries,75)  # 75th percentile
# iqr  = q3 - q1                     # Interquartile Range
 
# print(f'Std Deviation: {std:.2f}K  (most important spread measure)')
# print(f'IQR: {iqr}K  (Q1={q1}, Q3={q3})')
 
# # Outlier detection using IQR
# lower = q1 - 1.5*iqr
# upper = q3 + 1.5*iqr
# outliers = [x for x in salaries if x < lower or x > upper]
# print(f'Outliers: {outliers}')


import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
 
np.random.seed(42)
study  = np.random.uniform(2, 10, 60)
marks  = study * 8 + np.random.normal(0, 10, 60)
marks  = np.clip(marks, 30, 100)
absent = 10 - study + np.random.normal(0, 1, 60)
 
df = pd.DataFrame({'Study_Hours':study,'Marks':marks,'Absences':absent})
 
corr_matrix = df.corr()
print(corr_matrix.round(3))
 
plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f')
plt.title('Correlation Matrix'); plt.show()
 
# Pearson correlation
r, p_value = stats.pearsonr(study, marks)
print(f'Study-Marks correlation: r={r:.3f}, p={p_value:.4f}')
print('Interpretation:', 'Strong positive' if r>0.7 else 'Moderate' if r>0.4 else 'Weak')
