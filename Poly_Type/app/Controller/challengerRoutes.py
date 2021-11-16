from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request, session
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.datastructures import ContentSecurityPolicy
from werkzeug.routing import IntegerConverter
from app.Model.models import Challenge, Host, Prompt, Result
from app import db
from config import Config
from app.Controller.forms import CreateChallengeForm, RegistrationForm, JoinChallengeForm, LoginForm
import random
import string
import uuid
import json

challenger_routes = Blueprint('challenger', __name__)
challenger_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'

@challenger_routes.route('/', methods=['GET', 'POST'])
@challenger_routes.route('/index', methods=['GET', 'POST'])
def index():
    joinForm = JoinChallengeForm()
    loginForm = LoginForm()
    registrationForm = RegistrationForm()

    if request.method == 'POST':
        #If statements confirm the form that was submitted, and then validate it. Redirect behavior is temporary until routes are further developed. 
        if request.form["submit"] == "Join" and joinForm.validate_on_submit():
            guid = uuid.uuid4().hex
            # have to use upper on the join code string because the UI doesn't force the form to send only uppercase letters
            challenge = Challenge.query.filter_by(joincode=joinForm.joincode.data.upper()).first()
            if challenge is not None and challenge.open:
                session[guid] = (challenge.id, joinForm.nickname.data)
                #print("Joined Challenge {} with nickname {}".format(joinForm.joincode.data, joinForm.nickname.data))
                return redirect(url_for('challenger.take_challenge', guid=guid))
            flash(f'The room {joinForm.joincode.data} is not open or does not exist')
            # this print statement is here so I can see if this hits correctly, currently flash messages are not set up
            print(f'The room {joinForm.joincode.data} is not open or does not exist')
        
        if request.form["submit"] == "Login" and loginForm.validate_on_submit():
            user = Host.query.filter_by(username=loginForm.username.data).first()
            if user is None or not user.check_password(loginForm.password.data):
                print("Invalid username or password")
                flash('Invalid username or password')
                return redirect(url_for('challenger.index'))
            print("Logged in as {}".format(loginForm.username.data))
            login_user(user)
            return redirect(url_for('host.view_challenges'))
        
        if request.form["submit"] == "Register" and registrationForm.validate_on_submit():
            host = Host(username = registrationForm.reg_username.data)
            host.set_password(registrationForm.reg_password.data)
            db.session.add(host)
            db.session.commit()
            login_user(host)
            return redirect(url_for('host.view_challenges'))
    return render_template('index.html', joinForm = joinForm, loginForm = loginForm, registrationForm = registrationForm)

@challenger_routes.route('/take_challenge/<guid>', methods=['GET', 'POST'])
def take_challenge(guid):
    if request.method == "POST":
        resultsDict = json.loads(request.data.decode('utf-8'))
        currentChallenge = Challenge.query.filter_by(id = session[guid][0]).first()
        wpm = ((int(resultsDict["correctLetters"]) / 5) / (int(resultsDict["elapsedTime"]) / 60000))
        result = Result(elapsedTime = resultsDict["elapsedTime"], correct = resultsDict["correctLetters"], 
            incorrect = resultsDict["incorrectLetters"], extra = resultsDict["extraLetters"], 
            challenger = session[guid][1], wpm = wpm)        
        currentChallenge.results.append(result)
        db.session.commit()
        session[guid] = (result.id, session[guid][1])
        return redirect(url_for('challenger.results', guid=guid))
    
    challengeId = session[guid][0]
    challenge = Challenge.query.filter_by(id=challengeId).first()
    nickname = session[guid][1]
    return render_template("takechallenge.html", challenge=challenge, nickname=nickname)

@challenger_routes.route('/results/<guid>', methods=['GET'])
def results(guid):
    result = Result.query.filter_by(id = session[guid][0]).first()
    return render_template("challengerResult.html", result = result, nickname = session[guid][1])

