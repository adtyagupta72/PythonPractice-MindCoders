import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
 
nltk.download('punkt'); 
nltk.download('stopwords'); 
nltk.download('wordnet')
nltk.download('punkt_tab')  # newer NLTK versions
 
text = 'Students are learning Python for AI and Machine Learning in Bhopal!'
 
# Step 1: Tokenise — split into words
tokens = word_tokenize(text.lower())
print('Tokens:', tokens)
 
# Step 2: Remove stopwords (common words that add no meaning)
stop = set(stopwords.words('english'))
filtered = [w for w in tokens if w not in stop and w.isalpha()]
print('After stopword removal:', filtered)

# Step 3: Lemmatise — reduce to root form
lemma = WordNetLemmatizer()
final = [lemma.lemmatize(w) for w in filtered]
print('After lemmatisation:', final)
 
# TF-IDF — convert text to numbers for ML
from sklearn.feature_extraction.text import TfidfVectorizer
docs = ['Python is great for data science','Machine learning is amazing','AI is the future of technology']
tfidf = TfidfVectorizer()
matrix = tfidf.fit_transform(docs)
print('TF-IDF shape:', matrix.shape)  # (3 docs, N unique words)
print('Feature names:', tfidf.get_feature_names_out())
