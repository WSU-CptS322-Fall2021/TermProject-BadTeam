from datetime import datetime
from sqlalchemy.sql.schema import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin
from app import login

class Host(UserMixin, db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    challenges = db.relationship('Challenge', backref='host', lazy='dynamic')

    def __repr__(self):
        return f'<Host {self.id} - {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return Host.query.get(int(id))
    
    def get_host_challenges(self):
        return self.challenges

    def get_host_id(self):
        return self.id

class Challenge(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    host_id = db.Column(db.Integer, db.ForeignKey('host.id'))
    title = db.Column(db.String(64))
    joincode = db.Column(db.String(6))
    prompts = db.relationship('Prompt', backref='challenge', lazy='dynamic')
    results = db.relationship('Result', backref='challenge', lazy='dynamic')
    open = db.Column(db.Boolean)
    #host exists as a backref to its host object

    def __repr__(self):
        return f'<Challenge {self.id} - Title: {self.title} - JoinCode: {self.joincode} - Open: {self.open}>'

class Prompt(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    text = db.Column(db.String(3000))
    challenge_id =db.Column(db.Integer, db.ForeignKey('challenge.id'))
    #challenge exists as a backref to its challenge object

    def __repr__(self):
        return f'<Prompt {self.id} - Text: {self.text} - ChallengeId: {self.challenge_id}>'

class Result(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    challenger = db.Column(db.String(64))
    elapsedTime = db.Column(db.Integer)
    correct = db.Column(db.Integer)
    incorrect = db.Column(db.Integer)
    extra = db.Column(db.Integer)
    wpm = db.Column(db.Integer)
    challenge_id =db.Column(db.Integer, db.ForeignKey('challenge.id'))
    #challenge exists as a backref to its challenge object

    def __repr__(self):
        return f'<Result {self.id} - Challenger: {self.challenger} - ElapsedTime: {self.elapsedTime} - #Correct: {self.correct} - #Inorrect: {self.incorrect}>'



