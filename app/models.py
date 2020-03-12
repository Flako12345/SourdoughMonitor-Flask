from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
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

    def get_readings(self):
        sourdoughs = current_user.sourdoughs
        sourdoughIds = [sourdough.id for sourdough in sourdoughs]
        readings = Reading.query.filter(Reading.sourdough_id.in_(sourdoughIds)).all()

        return readings

    def get_feedings(self):
        sourdoughs = current_user.sourdoughs
        sourdoughIds = [sourdough.id for sourdough in sourdoughs]
        feedings = Feeding.query.filter(Feeding.sourdough_id.in_(sourdoughIds)).all()

        return feedings

    @staticmethod
    def insert_test_user():
        test_user = User(email='Test')
        test_user.set_password('password')
        db.session.add(test_user)
        db.session.commit()





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
    readings = db.relationship('Reading', backref='feeding', lazy='dynamic')

    def __repr__(self):
        return 'Fed {} at {}'.format(self.sourdough.name, self.timestamp)


class Reading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    reading = db.Column(db.Integer, nullable=False)
    normalizedReading = db.Column(db.Numeric, nullable=True)
    feeding_id = db.Column(db.Integer, db.ForeignKey('feeding.id'))
    sourdough_id = db.Column(db.Integer, db.ForeignKey('sourdough.id'))
    filename = db.Column(db.String(100))

    @staticmethod
    def from_json(json_reading):
        reading = json_reading.get('reading')
        sourdough_Id = json_reading.get('sourdough_id')
        filename = json_reading.get('filename')
        return Reading(reading=reading, sourdough_id=sourdough_Id, filename=filename)











@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))