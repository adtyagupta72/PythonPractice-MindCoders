import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Study hours vs exam marks
study = [1,2,3,4,5,6,7,8,9,10,2.5,4.5,6.5,8.5]
marks = [25,38,52,65,71,78,85,89,93,96,43,68,82,91]
 
X = np.array(study).reshape(-1,1)   # Must be 2D for sklearn
y = np.array(marks)
 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
 
model = LinearRegression()
model.fit(X_train, y_train)           # LEARNING happens here
 
print(f'Slope:     {model.coef_[0]:.2f}  (marks increase per study hour)')
print(f'Intercept: {model.intercept_:.2f} (marks at 0 study hours)')
 
y_pred = model.predict(X_test)
print(f'R² Score: {r2_score(y_test,y_pred):.4f} (1.0 = perfect)')
print(f'RMSE:     {mean_squared_error(y_test,y_pred)**0.5:.2f} marks average error')
 
# Predict new student
new_pred = model.predict([[7]])[0]
print(f'Student studying 7 hrs predicted marks: {new_pred:.1f}')
 
# Plot
plt.figure(figsize=(9,5))
plt.scatter(X,y,color='steelblue',s=100,alpha=0.8,label='Actual')
plt.plot(X,model.predict(X),color='red',linewidth=2,label='Predicted line')
plt.xlabel('Study Hours/Day'); plt.ylabel('Exam Marks')
plt.title('Linear Regression — Study Hours vs Marks')
plt.legend(); plt.grid(True,alpha=0.3); plt.show()