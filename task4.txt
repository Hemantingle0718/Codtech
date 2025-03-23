# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
# We will use the SMS Spam Collection dataset from the UCI repository

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip'

# Load the dataset (assuming you have the 'SMSSpamCollection' file locally or using a direct download)
df = pd.read_csv('SMSSpamCollection', sep='\t', header=None, names=["Label", "Message"])

# Check the first few rows of the dataset
df.head()

# Data Preprocessing
# Convert labels to binary: 'spam' -> 1, 'ham' -> 0
df['Label'] = df['Label'].map({'spam': 1, 'ham': 0})

# Check for missing values
df.isnull().sum()

# Exploratory Data Analysis (EDA)
# Visualizing the distribution of spam vs ham messages
plt.figure(figsize=(6, 4))
sns.countplot(x='Label', data=df, palette='viridis')
plt.title('Distribution of Spam vs Ham Messages')
plt.xlabel('Label (0: Ham, 1: Spam)')
plt.ylabel('Count')
plt.show()

# Explore the distribution of message lengths
df['Length'] = df['Message'].apply(len)
plt.figure(figsize=(10, 6))
sns.histplot(df[df['Label'] == 0]['Length'], color='blue', kde=True, label='Ham', bins=30)
sns.histplot(df[df['Label'] == 1]['Length'], color='red', kde=True, label='Spam', bins=30)
plt.legend()
plt.title('Distribution of Message Lengths by Label')
plt.xlabel('Length of Message')
plt.ylabel('Frequency')
plt.show()

# Split the dataset into features and target
X = df['Message']  # Features (text messages)
y = df['Label']    # Target (spam/ham labels)

# Train-Test Split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Text Preprocessing and Vectorization using TF-IDF (Term Frequency-Inverse Document Frequency)
vectorizer = TfidfVectorizer(stop_words='english')  # Remove stop words

X_train_tfidf = vectorizer.fit_transform(X_train)  # Learn vocabulary and transform training data
X_test_tfidf = vectorizer.transform(X_test)       # Transform test data

# Model Training - Using Multinomial Naive Bayes Classifier
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Make predictions
y_pred = model.predict(X_test_tfidf)

# Model Evaluation
# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')

# Confusion Matrix
plt.figure(figsize=(6, 6))
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap='Blues', xticklabels=['Ham', 'Spam'], yticklabels=['Ham', 'Spam'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, target_names=['Ham', 'Spam']))