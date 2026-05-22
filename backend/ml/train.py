import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

# Ensure the trained_model directory exists
MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'trained_model')
os.makedirs(MODEL_DIR, exist_ok=True)

def train_model():
    print("Loading dataset...")
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'dataset', 'dataset.csv')
    df = pd.read_csv(data_path)
    
    X = df['subject']
    y = df['category']
    
    print("Training model...")
    # Create a pipeline with TF-IDF and Logistic Regression
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000, stop_words='english')),
        ('clf', LogisticRegression(random_state=42, max_iter=1000))
    ])
    
    pipeline.fit(X, y)
    
    print("Evaluating model...")
    accuracy = pipeline.score(X, y)
    print(f"Training Accuracy: {accuracy * 100:.2f}%")
    
    # Save the pipeline
    model_path = os.path.join(MODEL_DIR, 'classifier.pkl')
    joblib.dump(pipeline, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model()
