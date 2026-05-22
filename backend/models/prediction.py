from backend.extensions import db
from datetime import datetime

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_text = db.Column(db.Text, nullable=False)
    predicted_category = db.Column(db.String(50), nullable=False)
    confidence_score = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Prediction('{self.predicted_category}', '{self.confidence_score}')"
    
    def to_dict(self):
        return {
            'id': self.id,
            'subject_text': self.subject_text,
            'predicted_category': self.predicted_category,
            'confidence_score': self.confidence_score,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
