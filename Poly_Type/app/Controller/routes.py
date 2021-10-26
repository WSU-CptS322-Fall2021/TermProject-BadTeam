from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app.Model.models import Host
from app import db
from config import Config
from app.Controller.forms import CreateChallengeForm, RegistrationForm, JoinChallengeForm, LoginForm

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'

@bp_routes.route('/', methods=['GET', 'POST'])
@bp_routes.route('/index', methods=['GET', 'POST'])
def index():
    joinForm = JoinChallengeForm()
    loginForm = LoginForm()
    registrationForm = RegistrationForm()

    if request.method == 'POST':
        #If statements confirm the form that was submitted, and then validate it. Redirect behavior is temporary until routes are further developed. 
        if request.form["submit"] == "Join" and joinForm.validate_on_submit():
            print("Joined Challenge {} with nickname {}".format(joinForm.joincode.data, joinForm.nickname.data))
            redirect(url_for('routes.index'))
        if request.form["submit"] == "Login" and loginForm.validate_on_submit():
            redirect(url_for('routes.index'))
        if request.form["submit"] == "Register" and registrationForm.validate_on_submit():
            redirect(url_for('routes.index'))

    return render_template('index.html', joinForm = joinForm, loginForm = loginForm, registrationForm = registrationForm)

@bp_routes.route('/createchallenge', methods=['GET', 'POST'])
def createChallenge():
    challengeForm = CreateChallengeForm()
    return render_template('createChallenge.html', challengeForm = challengeForm)
    
@bp_routes.route('/takechallenge', methods=['GET','POST'])
def takeChallenge():
    #For now I'm just passing a hard coded string. This will need to be a lot more advanced in the long run.
    demoPrompt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    return render_template('takeChallenge.html', prompt=demoPrompt)
