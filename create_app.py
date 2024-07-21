from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from models import User, Lead, UserActionLog  # Убедитесь, что путь к файлу models правильный

    from auth.routes import auth  # Убедитесь, что путь к модулю auth правильный
    app.register_blueprint(auth)

    return app
