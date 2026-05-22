# pyrefly: ignore [missing-import]
from functools import wraps
from flask import render_template, redirect, url_for, flash, Blueprint
from backend.extensions import db
from flask_login import login_required, current_user
from sqlalchemy import func
from backend.models.user import User
from backend.models.prediction import Prediction

admin = Blueprint('admin', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('main.dashboard'))
        return f(*args, **kwargs)
    return decorated_function

@admin.route('/')
@login_required
@admin_required
def index():
    total_users = User.query.count()
    total_preds = Prediction.query.count()
    category_distribution = db.session.query(
        Prediction.predicted_category, func.count(Prediction.id)
    ).group_by(Prediction.predicted_category).all()
    
    return render_template('admin.html', total_users=total_users, total_preds=total_preds, category_distribution=category_distribution)
