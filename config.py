import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-gulshan-ai-key-998877'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///gulshan_ai.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Model Paths
    MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trained_model', 'classifier.pkl')
    VECTORIZER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trained_model', 'vectorizer.pkl')
