import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
import tkinter as tk
from tkinter import messagebox

def load_data(train_path, test_path):
    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)
    return train_data, test_data

def visualize_training(train_data):
    # Visualize the distribution of sentiments in the training dataset
    plt.figure(figsize=(8, 6))
    sns.countplot(data=train_data, x='label')
    plt.title('Distribution of Sentiments in Training Data')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

def extract_features(train_data,test_data):
    # Extract features and labels from the training dataset
    X_train_raw = train_data['tweet']  # Tweets
    y_train = train_data['label']    # Sentiment labels
    X_test_raw = test_data['tweet']
    return X_train_raw, y_train, X_test_raw

def preprocess(X_train_raw, X_test_raw):
    vectorizer = CountVectorizer(stop_words='english', max_features=5000)
    X_train = vectorizer.fit_transform(X_train_raw)
    X_test = vectorizer.transform(X_test_raw)
    return X_train, X_test

def train(X_train, y_train):
    svm_model = SVC(kernel='linear', random_state=42)
    svm_model.fit(X_train, y_train)
    return svm_model

def predict(svm_model,X_test):
    y_pred = svm_model.predict(X_test)
    test_data.to_csv('predictions.csv', index=False)
    messagebox.showinfo("Prediction saved to predictions.csv.")
    return y_pred

def visualize_predictions(y_pred):  
    plt.figure(figsize=(8, 6))
    sns.countplot(x=y_pred, palette='cool')
    plt.title('Distribution of Predicted Sentiments')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

train_data, test_data = load_data('dataset/train.csv', 'dataset/test.csv')
print("Train Data Info:")
print(train_data.info())
print("\nTest Data Info:")
print(test_data.info())


X_train_raw, y_train, X_test_raw = extract_features(train_data, test_data)
print("X_train_raw:\n",X_train_raw)
print("y_tarin:\n",y_train)
print("x_test_raw:\n",X_test_raw)

X_train,X_test=preprocess(X_train_raw, X_test_raw)
print("Preprocessing Done.")

svm_model=train(X_train, y_train)

y_pred=predict(svm_model,X_test)

visualize_training(train_data)

visualize_predictions(y_pred)
