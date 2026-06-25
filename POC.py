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


# import numpy as np
# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy import stats
 
# np.random.seed(42)
# study  = np.random.uniform(2, 10, 60)
# marks  = study * 8 + np.random.normal(0, 10, 60)
# marks  = np.clip(marks, 30, 100)
# absent = 10 - study + np.random.normal(0, 1, 60)
 
# df = pd.DataFrame({'Study_Hours':study,'Marks':marks,'Absences':absent})
 
# corr_matrix = df.corr()
# print(corr_matrix.round(3))
 
# plt.figure(figsize=(6,4))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f')
# plt.title('Correlation Matrix'); plt.show()
 
# # Pearson correlation
# r, p_value = stats.pearsonr(study, marks)
# print(f'Study-Marks correlation: r={r:.3f}, p={p_value:.4f}')
# print('Interpretation:', 'Strong positive' if r>0.7 else 'Moderate' if r>0.4 else 'Weak')

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm
 
# # Normal Distribution — the bell curve
# # Heights of Indian males: mean=165cm, std=7cm
# mean_h, std_h = 165, 7
 
# # Probability of being taller than 175cm
# prob = 1 - norm.cdf(175, mean_h, std_h)
# print(f'P(height > 175cm) = {prob:.4f} = {prob*100:.1f}%')
 
# # The 68-95-99.7 Rule
# print(f'68% of people: {mean_h-std_h:.0f}cm to {mean_h+std_h:.0f}cm')
# print(f'95% of people: {mean_h-2*std_h:.0f}cm to {mean_h+2*std_h:.0f}cm')
# print(f'99.7% of people: {mean_h-3*std_h:.0f}cm to {mean_h+3*std_h:.0f}cm')
 
# # Outlier detection using Z-score (3-sigma rule)
# transactions = [250,310,280,5000,295,270,315,290,10000,305,285]
# mean_t = np.mean(transactions)
# std_t  = np.std(transactions)
# z_scores = [(x - mean_t)/std_t for x in transactions]
# flagged  = [x for x,z in zip(transactions,z_scores) if abs(z)>3]
# print(f'Flagged as outliers: {flagged}')  # [5000, 10000]

# from sklearn.model_selection import train_test_split, cross_val_score
# import numpy as np
 
# # Simulated dataset: 500 student records
# np.random.seed(42)
# X = np.random.randn(500, 5)   # 5 features (study hrs, attendance, etc.)
# y = np.random.randint(0,2,500) # Labels: pass(1)/fail(0)
 
# # 80/20 Train-Test Split
# X_train,X_test,y_train,y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42, stratify=y
# )
# print(f'Training samples: {len(X_train)} | Test samples: {len(X_test)}')
 
# # 5-Fold Cross-Validation — more reliable than single split
# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier(n_estimators=50, random_state=42)
# cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
# print(f'CV Scores each fold: {cv_scores.round(3)}')
# print(f'Mean: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}')


# Scenario: An e-commerce company tested two website layouts.
# Version A (old): 1000 visitors, 52 purchases
# Version B (new): 1000 visitors, 68 purchases
# Question: Is Version B ACTUALLY better, or could this be random chance?
 
# import numpy as np
# from scipy import stats
# import matplotlib.pyplot as plt
 
# # Data
# n_A, conv_A = 1000, 52
# n_B, conv_B = 1000, 68
# rate_A = conv_A / n_A
# rate_B = conv_B / n_B
 
# print(f'Version A conversion rate: {rate_A*100:.1f}%')
# print(f'Version B conversion rate: {rate_B*100:.1f}%')
# print(f'Improvement: {(rate_B-rate_A)/rate_A*100:.1f}%')
 
# # Chi-square test for statistical significance
# table = [[conv_A, n_A-conv_A],[conv_B, n_B-conv_B]]
# chi2, p_value, dof, expected = stats.chi2_contingency(table)
 
# print(f'Chi-square: {chi2:.4f}')
# print(f'P-value: {p_value:.4f}')
# print('Result:', 'SIGNIFICANT — B is better!' if p_value<0.05 else 'NOT significant — could be random')


# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score
 
# # Study hours vs exam marks
# study = [1,2,3,4,5,6,7,8,9,10,2.5,4.5,6.5,8.5]
# marks = [25,38,52,65,71,78,85,89,93,96,43,68,82,91]
 
# X = np.array(study).reshape(-1,1)   # Must be 2D for sklearn
# y = np.array(marks)
 
# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
 
# model = LinearRegression()
# model.fit(X_train, y_train)           # LEARNING happens here
 
# print(f'Slope:     {model.coef_[0]:.2f}  (marks increase per study hour)')
# print(f'Intercept: {model.intercept_:.2f} (marks at 0 study hours)')
 
# y_pred = model.predict(X_test)
# print(f'R² Score: {r2_score(y_test,y_pred):.4f} (1.0 = perfect)')
# print(f'RMSE:     {mean_squared_error(y_test,y_pred)**0.5:.2f} marks average error')
 
# # Predict new student
# new_pred = model.predict([[7]])[0]
# print(f'Student studying 7 hrs predicted marks: {new_pred:.1f}')
 
# # Plot
# plt.figure(figsize=(9,5))
# plt.scatter(X,y,color='steelblue',s=100,alpha=0.8,label='Actual')
# plt.plot(X,model.predict(X),color='red',linewidth=2,label='Predicted line')
# plt.xlabel('Study Hours/Day'); plt.ylabel('Exam Marks')
# plt.title('Linear Regression — Study Hours vs Marks')
# plt.legend(); plt.grid(True,alpha=0.3); plt.show()

# import pandas as pd
# import numpy as np
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# from sklearn.preprocessing import StandardScaler
# import seaborn as sns; import matplotlib.pyplot as plt
 
# # Generate student pass/fail dataset
# np.random.seed(42); n=300
# study   = np.random.uniform(1,10,n)
# attend  = np.random.uniform(40,100,n)
# tasks   = np.random.randint(0,11,n)
# score   = study*5 + attend*0.3 + tasks*2 + np.random.normal(0,8,n)
# passed  = (score > 65).astype(int)
 
# df = pd.DataFrame({'study':study,'attend':attend,'tasks':tasks,'passed':passed})
# X = df[['study','attend','tasks']]
# y = df['passed']
 
# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
 
# scaler = StandardScaler()
# Xtr = scaler.fit_transform(X_train)
# Xte = scaler.transform(X_test)
 
# model = LogisticRegression()
# model.fit(Xtr, y_train)
 
# y_pred = model.predict(Xte)
# print(f'Accuracy: {accuracy_score(y_test,y_pred)*100:.1f}%')
# print(classification_report(y_test,y_pred,target_names=['Fail','Pass']))
 
# # Confusion matrix
# cm = confusion_matrix(y_test,y_pred)
# sns.heatmap(cm,annot=True,fmt='d',cmap='Blues',
#     xticklabels=['Fail','Pass'],yticklabels=['Fail','Pass'])
# plt.title('Confusion Matrix'); plt.show()
 
# # Predict new student
# new = scaler.transform([[7, 85, 9]])  # 7hrs study, 85% attend, 9 tasks
# pred = model.predict(new)[0]
# prob = model.predict_proba(new)[0]
# print(f'Prediction: {"PASS" if pred==1 else "FAIL"} | Probability: {prob[1]*100:.1f}%')


# from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import matplotlib.pyplot as plt
 
# iris = load_iris()
# X,y  = iris.data, iris.target
# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
 
# # Decision Tree
# dt = DecisionTreeClassifier(max_depth=3,random_state=42)
# dt.fit(X_train,y_train)
# print(f'Decision Tree Accuracy: {accuracy_score(y_test,dt.predict(X_test))*100:.1f}%')
# print(export_text(dt,feature_names=list(iris.feature_names)))  # See the rules!
 
# # Visualise tree
# plt.figure(figsize=(14,6))
# plot_tree(dt,feature_names=iris.feature_names,class_names=iris.target_names,
#           filled=True,rounded=True,fontsize=9)
# plt.title('Decision Tree — Iris Classification'); plt.show()
 
# # Random Forest — multiple trees vote
# rf = RandomForestClassifier(n_estimators=100,random_state=42)
# rf.fit(X_train,y_train)
# print(f'Random Forest Accuracy: {accuracy_score(y_test,rf.predict(X_test))*100:.1f}%')
 
# # Feature importance — which inputs matter most?
# import pandas as pd
# imp = pd.Series(rf.feature_importances_,index=iris.feature_names).sort_values(ascending=False)
# imp.plot(kind='bar',color='steelblue')
# plt.title('Feature Importance'); plt.tight_layout(); plt.show()

# pip install xgboost
# from xgboost import XGBClassifier
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import pandas as pd
 
# data = load_breast_cancer()
# X = pd.DataFrame(data.data, columns=data.feature_names)
# y = data.target
 
# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
 
# xgb = XGBClassifier(n_estimators=100, max_depth=4, learning_rate=0.1,
#                     random_state=42, eval_metric='logloss', verbosity=0)
# xgb.fit(X_train,y_train)
# print(f'XGBoost Accuracy: {accuracy_score(y_test,xgb.predict(X_test))*100:.2f}%')

from tensorflow import keras
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
 
# Load MNIST: 70,000 handwritten digit images (28x28 pixels, grayscale)
(X_train,y_train),(X_test,y_test) = keras.datasets.mnist.load_data()
print(f'Training: {X_train.shape} | Test: {X_test.shape}')
 
# Visualise samples
plt.figure(figsize=(12,2))
for i in range(12):
    plt.subplot(1,12,i+1)
    plt.imshow(X_train[i],cmap='gray'); plt.axis('off')
    plt.title(str(y_train[i]),fontsize=8)
plt.suptitle('Sample MNIST Digits'); plt.show()
 
# Normalise: 0-255 → 0-1 (faster training, better convergence)
X_train = X_train / 255.0
X_test  = X_test  / 255.0
 
# Flatten 28x28 → 784 (1D vector)
X_train = X_train.reshape(-1, 784)
X_test  = X_test.reshape(-1, 784)
 
# Build neural network
model = keras.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),           # Randomly disable 20% neurons to prevent overfitting
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10,  activation='softmax')  # 10 output neurons for digits 0-9
])
 
model.summary()  # See architecture: layers, shapes, parameters
 
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
 
# Train the model
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=128,
    validation_split=0.1,
    callbacks=[keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)]
)
 
# Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f'Test Accuracy: {test_acc*100:.2f}%')
 
# Plot training history
fig, axes = plt.subplots(1,2,figsize=(12,4))
axes[0].plot(history.history['accuracy'],    label='Train')
axes[0].plot(history.history['val_accuracy'],label='Validation')
axes[0].set_title('Accuracy'); axes[0].legend()
axes[1].plot(history.history['loss'],    label='Train')
axes[1].plot(history.history['val_loss'],label='Validation')
axes[1].set_title('Loss'); axes[1].legend()
plt.tight_layout(); plt.show()
 
# See predictions on test images
predictions = model.predict(X_test[:15])
pred_classes = np.argmax(predictions, axis=1)
 
plt.figure(figsize=(15,3))
for i in range(15):
    plt.subplot(1,15,i+1)
    plt.imshow(X_test[i].reshape(28,28),cmap='gray')
    correct = pred_classes[i]==y_test[i]
    plt.title(str(pred_classes[i]), color='green' if correct else 'red', fontsize=8)
    plt.axis('off')
plt.suptitle('Green=Correct  Red=Wrong'); plt.show()
