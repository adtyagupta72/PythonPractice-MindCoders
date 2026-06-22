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

from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
 
iris = load_iris()
X,y  = iris.data, iris.target
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
 
# Decision Tree
dt = DecisionTreeClassifier(max_depth=3,random_state=42)
dt.fit(X_train,y_train)
print(f'Decision Tree Accuracy: {accuracy_score(y_test,dt.predict(X_test))*100:.1f}%')
print(export_text(dt,feature_names=list(iris.feature_names)))  # See the rules!
 
# Visualise tree
plt.figure(figsize=(14,6))
plot_tree(dt,feature_names=iris.feature_names,class_names=iris.target_names,
          filled=True,rounded=True,fontsize=9)
plt.title('Decision Tree,  Iris Classification'); plt.show()
 
# Random Forest,  multiple trees vote
rf = RandomForestClassifier(n_estimators=100,random_state=42)
rf.fit(X_train,y_train)
print(f'Random Forest Accuracy: {accuracy_score(y_test,rf.predict(X_test))*100:.1f}%')
 
# Feature importance,  which inputs matter most?
import pandas as pd
imp = pd.Series(rf.feature_importances_,index=iris.feature_names).sort_values(ascending=False)
imp.plot(kind='bar',color='steelblue')
plt.title('Feature Importance'); plt.tight_layout(); plt.show()
