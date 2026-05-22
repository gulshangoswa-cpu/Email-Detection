from flask import render_template, send_file, Blueprint, Response
from flask_login import login_required, current_user
from backend.models.prediction import Prediction
from backend.extensions import db
from sqlalchemy import func
import csv
import io

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    total_preds = Prediction.query.filter_by(user_id=current_user.id).count()
    
    # Get most predicted category
    most_common_cat_query = db.session.query(Prediction.predicted_category, func.count(Prediction.id).label('count')) \
                            .filter_by(user_id=current_user.id) \
                            .group_by(Prediction.predicted_category) \
                            .order_by(func.count(Prediction.id).desc()).first()
                            
    most_common = most_common_cat_query[0] if most_common_cat_query else 'N/A'
    
    recent_preds = Prediction.query.filter_by(user_id=current_user.id).order_by(Prediction.created_at.desc()).limit(5).all()
    
    return render_template('dashboard.html', total_preds=total_preds, most_common=most_common, recent_preds=recent_preds)

@main.route('/history')
@login_required
def history():
    preds = Prediction.query.filter_by(user_id=current_user.id).order_by(Prediction.created_at.desc()).all()
    return render_template('history.html', predictions=preds)

@main.route('/export')
@login_required
def export():
    preds = Prediction.query.filter_by(user_id=current_user.id).all()
    
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Date', 'Subject', 'Category', 'Confidence Score (%)'])
    
    for p in preds:
        writer.writerow([p.created_at.strftime('%Y-%m-%d %H:%M:%S'), p.subject_text, p.predicted_category, p.confidence_score])
        
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=prediction_history.csv"}
    )
