from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request, session
from flask_login import current_user, login_user, login_required
#from Poly_Type.app.Model.models import Challenge
from app.Model.models import Challenge, Host, Prompt
from app import db
from config import Config
from app.Controller.forms import CreateChallengeForm, RegistrationForm, JoinChallengeForm, LoginForm
import random
import string
import uuid

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
            guid = uuid.uuid4().hex
            # have to use upper on the join code string because the UI doesn't force the form to send only uppercase letters
            challenge = Challenge.query.filter_by(joincode=joinForm.joincode.data.upper()).first()
            if challenge is not None and challenge.open:
                session[guid] = (challenge.id, joinForm.nickname.data)
                print("Joined Challenge {} with nickname {}".format(joinForm.joincode.data, joinForm.nickname.data))
                return redirect(url_for('routes.takechallenge', guid=guid))
            flash(f'The room {joinForm.joincode.data} is not open or does not exist')
            # this print statement is here so I can see if this hits correctly, currently flash messages are not set up
            print(f'The room {joinForm.joincode.data} is not open or does not exist')
        
        if request.form["submit"] == "Login" and loginForm.validate_on_submit():
            user = Host.query.filter_by(username=loginForm.username.data).first()
            if user is None or not user.check_password(loginForm.password.data):
                print("Invalid username or password")
                flash('Invalid username or password')
                return redirect(url_for('routes.index'))
            print("Logged in as {}".format(loginForm.username.data))
            login_user(user)
            return redirect(url_for('routes.createChallenge'))
        
        if request.form["submit"] == "Register" and registrationForm.validate_on_submit():

            host = Host(username = registrationForm.reg_username.data)
            host.set_password(registrationForm.reg_password.data)
            db.session.add(host)
            db.session.commit()
            return redirect(url_for('routes.index'))
    return render_template('index.html', joinForm = joinForm, loginForm = loginForm, registrationForm = registrationForm)



def createCode():
    code = ''
    for i in range(0, 6):
        #Create a random capital letter
        randChar = random.choice(string.ascii_uppercase)
        #if the random int is 1 and not 'O' or 'I' add it
        if (random.randint(0, 1) == 1) and (randChar != 'I') and (randChar != 'O'):
            code += randChar
        else:
            #add a random digit if random int is 0
            code += random.choice(string.digits)

    return code

@bp_routes.route('/createchallenge', methods=['GET', 'POST'])
@login_required
def createChallenge():
    form = CreateChallengeForm()
    if form.validate_on_submit():
        #Creates a random join code
        code = createCode()
        
        #If random code is already used keep looping until it finds one that is not used
        while Challenge.query.filter_by(joincode=code).first() != None:
            code = createCode()
        
        #Create a new challenge with the random code
        #TODO: The value of the host is currently hardcoded because we do not have a currently logged in user to set the value of host id to
        #TODO: Currently, we are allowing for individuals to make challenges with the same name, we should fix this when we have the user logged in
        newChallenge = Challenge(joincode=code, open=False, host_id=1, title=form.title.data)
        
        # Scan through all prompts and append them if there is text
        for promptForm in form.prompts.data:
            if promptForm["prompt"] is not None:
                prompt = Prompt(text=promptForm["prompt"])
                newChallenge.prompts.append(prompt)

        print("Created Challenge: Room Code {}".format(newChallenge.joincode))
        db.session.add(newChallenge)
        db.session.commit()
        #TODO: Consider whether flash messages are desire or needed at all.
        #flash('Challenge created!')
        return redirect(url_for('routes.viewchallenges'))
    return render_template('createChallenge.html', challengeForm = form)
    
@bp_routes.route('/takechallenge/<guid>', methods=['GET', 'POST'])
def takechallenge(guid):
    challengeId = session[guid][0]
    challenge = Challenge.query.filter_by(id=challengeId).first()
    nickname = session[guid][1]
    return render_template("takechallenge.html", challenge=challenge, nickname=nickname)

@bp_routes.route('/viewchallenges', methods=['GET', 'POST'])
def viewchallenges():
    #TODO: Once we have authentication we need to integrate it in here to load in only current use
    challenges = Challenge.query.all()
    return render_template("viewchallenges.html", challenges=challenges)

@bp_routes.route('/openchallenge/<challengeid>', methods=['POST'])
def openChallenge(challengeid):
    challenge = Challenge.query.filter_by(id = challengeid).first()
    if not challenge == None:
        challenge.open = True
        db.session.add(challenge)
        db.session.commit()
        return redirect(url_for('routes.viewchallenges'))

@bp_routes.route('/closeChallenge/<challengeid>', methods=['POST'])
def closeChallenge(challengeid):
    challenge = Challenge.query.filter_by(id = challengeid).first()
    if not challenge == None:
        challenge.open = False
        db.session.add(challenge)
        db.session.commit()
        return redirect(url_for('routes.viewchallenges'))
