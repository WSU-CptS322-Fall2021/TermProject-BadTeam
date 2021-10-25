from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
#from Poly_Type.app.Model.models import Challenge
from app.Model.models import Challenge
from app.Model.models import Host
from app import db
from config import Config
from app.Controller.forms import CreateChallengeForm, RegistrationForm, TakeChallengeForm, LoginForm
import random
import string

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


def createCode():
    code = ''
    for i in range(0, 5):
        randChar = random.choice(string.ascii_uppercase)#Create a random capital letter
        if((random.randint(0, 1) == 1) and (randChar != 'I') and (randChar != 'O')):#if the random int is 1 and not 'O' or 'I' add it
            code += randChar
        else:#add a random digit if random int is 0
            code += random.choice(string.digits)

    return code

@bp_routes.route('/createchallenge', methods=['GET', 'POST'])
#@login_required
def createChallenge():
    challengeForm = CreateChallengeForm()

    if challengeForm.validate_on_submit():
        code = createCode()#Creates a random code
        while((db.session.query.filter_by(joincode=code).first()) != None):#If random code is already used keep looping until it finds one that is not used
            code = createCode()
        
        challenge = Challenge(joincode = code, open=False, host_id= Host.id)#Create a new challenge with the random code
        for t in challengeForm.challenge.data:
            if t.prompt is not None:
                challenge.challenges.append(t)
        db.session.add(challenge)
        db.session.commit()
        flash('Challenge created!')
        print("Challenge created with code {}".format(code))
        return redirect(url_for('routes.index'))
    return render_template('createChallenge.html', challengeForm = challengeForm)
    

