# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm	#Normal Distribution calculator

# #You feed it a mean and standard deviation, and it can answer any probability question about that distribution instantly.

# # Normal Distribution — the bell curve
# # Normal distribution with mean 165cm and standard deviation 7cm.
# mean_h, std_h = 165, 7
 
# # Probability of being taller than 175cm
# prob = 1 - norm.cdf(175, mean_h, std_h) # Cumulative distribution function, tells how many people are shorter or equals to 175, as we want taller than 175, so 1 - cdf is done.
# print(f'P(height > 175cm) = {prob:.4f} = {prob*100:.1f}%')
 
# # The 68-95-99.7 Rule
# print(f'68% of people: {mean_h-std_h:.0f}cm to {mean_h+std_h:.0f}cm')
# print(f'95% of people: {mean_h-2*std_h:.0f}cm to {mean_h+2*std_h:.0f}cm')
# print(f'99.7% of people: {mean_h-3*std_h:.0f}cm to {mean_h+3*std_h:.0f}cm')

# from sklearn.model_selection import train_test_split, cross_val_score
# import numpy as np
# #python -m pip install scikit-learn
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
 
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
 
# Data
n_A, conv_A = 1000, 52
n_B, conv_B = 1000, 68
rate_A = conv_A / n_A
rate_B = conv_B / n_B
 
print(f'Version A conversion rate: {rate_A*100:.1f}%')
print(f'Version B conversion rate: {rate_B*100:.1f}%')
print(f'Improvement: {(rate_B-rate_A)/rate_A*100:.1f}%')

# Chi-square test for statistical significance
table = [[conv_A, n_A-conv_A],[conv_B, n_B-conv_B]]
chi2, p_value, dof, expected = stats.chi2_contingency(table)
 
print(f'Chi-square: {chi2:.4f}')
print(f'P-value: {p_value:.4f}')
print('Result:', 'SIGNIFICANT — B is better!' if p_value<0.05 else 'NOT significant — could be random')

