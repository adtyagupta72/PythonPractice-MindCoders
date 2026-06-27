from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
 
# Training data: product reviews
reviews = [
    ('This product is absolutely amazing! Highly recommend!', 1),
    ('Great quality and fast delivery. Very happy!', 1),
    ('Excellent value for money. Works perfectly!', 1),
    ('Loved it! Will definitely buy again.', 1),
    ('Super satisfied with this purchase!', 1),
    ('Five stars! Outstanding product!', 1),
    ('Terrible quality. Broke after 2 days.', 0),
    ('Worst purchase ever. Complete waste of money!', 0),
    ('Very disappointed. Not as described at all.', 0),
    ('Horrible experience. Never buying again.', 0),
    ('Poor quality and very late delivery.', 0),
    ('Total scam. Do not buy this product.', 0),
]
 
texts, labels = zip(*reviews)
 
vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=500)
X = vectorizer.fit_transform(texts)
y = list(labels)
 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42)
 
clf = LogisticRegression()
clf.fit(X_train, y_train)
print(f'Accuracy: {accuracy_score(y_test,clf.predict(X_test))*100:.0f}%')
 
# Test on new reviews
new = ['This is a wonderful product! Totally worth it!',
       'Very bad experience. Quality is awful.',
       'Average product. Nothing special.']
 
X_new = vectorizer.transform(new)
for review, pred, prob in zip(new, clf.predict(X_new), clf.predict_proba(X_new)):
    sentiment = 'POSITIVE' if pred==1 else 'NEGATIVE'
    confidence = max(prob)*100
    print(f'[{sentiment} {confidence:.0f}%] {review[:45]}...')
