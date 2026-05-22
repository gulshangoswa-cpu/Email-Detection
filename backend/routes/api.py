import os
import joblib
import numpy as np
from flask import jsonify, request, current_app, Blueprint
from flask_login import login_required, current_user
from backend.models.prediction import Prediction
from backend.extensions import db

api = Blueprint('api', __name__)

# Cache model
model = None

def get_model():
    global model
    if model is None:
        model_path = current_app.config['MODEL_PATH']
        if os.path.exists(model_path):
            model = joblib.load(model_path)
    return model

@api.route('/predict', methods=['POST'])
@login_required
def predict():
    data = request.get_json()
    if not data or 'subject' not in data:
        return jsonify({'error': 'Subject is required'}), 400
        
    subject = data['subject']
    classifier = get_model()
    
    if not classifier:
        return jsonify({'error': 'Model not trained yet. Please ask admin to train the model.'}), 500
        
    # Make prediction
    pred_category = classifier.predict([subject])[0]
    
    # Calculate confidence score
    probs = classifier.predict_proba([subject])[0]
    confidence = np.max(probs) * 100
    
    # Save to database
    prediction = Prediction(
        subject_text=subject,
        predicted_category=pred_category,
        confidence_score=confidence,
        author=current_user
    )
    db.session.add(prediction)
    db.session.commit()
    
    return jsonify({
        'category': pred_category,
        'confidence': f"{confidence:.1f}%"
    })
