# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
from scipy import stats #open-source Python library used for scientific, mathematical, and engineering computing
 
# # Employee salaries (in thousands Rs.)
# salaries = [22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]
 
# # Central Tendency - where is the 'centre' of data?
# mean   = np.mean(salaries)         # Average
# median = np.median(salaries)       # Middle value when sorted
# mode   = stats.mode(salaries,keepdims=True).mode[0]  # Most frequent
 
# print(f'Mean   (Average):     Rs.{mean:.1f}K')
# print(f'Median (Middle value): Rs.{median}K')
# print(f'Mode   (Most common):  Rs.{mode}K')

# # Spread - how varied is the data?
# std  = np.std(salaries)            # Standard deviation
# var  = np.var(salaries)            # Variance (std squared)
# rng  = max(salaries)-min(salaries) # Range
# q1   = np.percentile(salaries,25)  # 25th percentile
# q3   = np.percentile(salaries,75)  # 75th percentile
# iqr  = q3 - q1                     # Interquartile Range
 
# print(f'Std Deviation: {std:.2f}K  (most important spread measure)')
# print(f'IQR: {iqr}K  (Q1={q1}, Q3={q3})')

# # Outlier detection using IQR (Interquartile Range)
# lower = q1 - 1.5*iqr
# upper = q3 + 1.5*iqr
# outliers = [x for x in salaries if x < lower or x > upper]
# print(f'Outliers: {outliers}')


import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
 
# Data
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
