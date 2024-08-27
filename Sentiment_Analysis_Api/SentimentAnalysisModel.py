import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import nltk
from nltk.corpus import movie_reviews
import random

# Download NLTK data
nltk.download('movie_reviews')

# Load dataset
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

# Convert to DataFrame
df = pd.DataFrame(documents, columns=['text', 'label'])
df['text'] = df['text'].apply(lambda x: ' '.join(x))

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Create a pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
predicted = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predicted)}")

# Save the model
with open('sentiment_model.pkl', 'wb') as f:
    pickle.dump(model, f)
