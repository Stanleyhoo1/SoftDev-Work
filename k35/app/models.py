from datetime import datetime
from app import db, login
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    edits = db.relationship('Edit', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    completed = db.Column(db.Boolean, default=False)
    edits = db.relationship('Edit', backref='story', lazy='dynamic')

    def __repr__(self):
        return f'<Story {self.title}>'

class Edit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Edit {self.body[:50]}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))