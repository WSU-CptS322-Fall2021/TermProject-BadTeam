from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app.Model.models import Host
from app import db
from config import Config
from app.Controller.forms import CreateChallengeForm, RegistrationForm, TakeChallengeForm, LoginForm

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'

@bp_routes.route('/', methods=['GET', 'POST'])
@bp_routes.route('/index', methods=['GET', 'POST'])
def index():
    joinForm = TakeChallengeForm()
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
    

