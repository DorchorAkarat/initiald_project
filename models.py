
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    info = db.Column(db.Text)
    image = db.Column(db.Text)
    stage = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
