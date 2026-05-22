import os
from flask import Flask
from config import Config
from backend.extensions import db, bcrypt, login_manager
from backend.models.user import User

def create_app(config_class=Config):
    app = Flask(__name__, 
                template_folder='backend/templates',
                static_folder='backend/static')
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    from backend.routes.main import main
    from backend.routes.auth import auth
    from backend.routes.api import api
    from backend.routes.admin import admin

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(admin, url_prefix='/admin')

    with app.app_context():
        import backend.models
        db.create_all()
        # Optionally, create an admin user
        if not User.query.filter_by(username='admin').first():
            hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
            admin_user = User(username='admin', email='admin@gulshanai.com', password=hashed_password, is_admin=True)
            db.session.add(admin_user)
            db.session.commit()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000))

