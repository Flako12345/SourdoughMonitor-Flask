from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    sourdoughs = db.relationship('Sourdough', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def create_user(self):
        pass

    def login(self):
        pass

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Sourdough(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    birthday = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    feedings = db.relationship('Feeding', backref='sourdough', lazy='dynamic')
    readings = db.relationship('Reading', backref='sourdough', lazy='dynamic')
    alive = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Feeding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    sourdough_id = db.Column(db.Integer, db.ForeignKey('sourdough.id'), nullable=False)

    def __repr__(self):
        return 'Fed {} at {}'.format(self.sourdough.name, self.timestamp)


class Reading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    reading = db.Column(db.Integer, nullable=False)
    sourdough_id = db.Column(db.Integer, db.ForeignKey('sourdough.id'))

    @staticmethod
    def from_json(json_reading):
        reading = json_reading.get('reading')
        sourdough_Id = json_reading.get('sourdough_id')
        return Reading(reading=reading, sourdough_id=sourdough_Id)











@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))