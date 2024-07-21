# crm_app/models.py

from crm_app import db
from datetime import datetime
import bcrypt
from pydantic import BaseModel, ValidationError, constr

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)

class UserActionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    action = db.Column(db.String(150), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class UserValidation(BaseModel):
    username: constr(min_length=3, max_length=50)
    email: constr(regex=r'^\S+@\S+\.\S+$')

# Пример валидации
try:
    user = UserValidation(username='test', email='test@example.com')
except ValidationError as e:
    print(e.json())
