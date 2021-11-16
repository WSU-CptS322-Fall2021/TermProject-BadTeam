from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request, session
from flask_login import current_user, login_user, login_required, logout_user
from app.Model.models import Challenge, Host, Prompt
from app import db
from config import Config
from app.Controller.forms import CreateChallengeForm, RegistrationForm, JoinChallengeForm, LoginForm, UpdateInfoForm
import random
import string
import uuid

host_routes = Blueprint('host', __name__)
host_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'

@host_routes.route('/view_challenges', methods=['GET', 'POST'])
@login_required
def view_challenges():
    challenges = current_user.get_host_challenges()
    return render_template("viewchallenges.html", challenges=challenges)

@host_routes.route('/open_challenge/<challengeid>', methods=['POST'])
@login_required
def open_challenge(challengeid):
    challenge = Challenge.query.filter_by(id = challengeid).first()
    if not challenge == None:
        challenge.open = True
        db.session.add(challenge)
        db.session.commit()
        return redirect(url_for('host.view_challenges'))

@host_routes.route('/close_challenge/<challengeid>', methods=['POST'])
@login_required
def close_challenge(challengeid):
    challenge = Challenge.query.filter_by(id = challengeid).first()
    if not challenge == None:
        challenge.open = False
        db.session.add(challenge)
        db.session.commit()
        return redirect(url_for('host.view_challenges'))

@host_routes.route('/update_info', methods=['GET', 'POST'])
@login_required
def update_info(): #If the user is a host, allow them to update their information
    form = UpdateInfoForm()
    if form.validate_on_submit():
        host = Host.query.filter_by(id = current_user.id).first()
        host.username = form.reg_username.data
        host.set_password(form.reg_password.data)
        db.session.merge(host)
        db.session.commit()
        flash('Your information has been updated!')
        return redirect(url_for('host.view_challenges'))
    return render_template('updateinfo.html', form=form)


@host_routes.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('challenger.index'))

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

@host_routes.route('/create_challenge', methods=['GET', 'POST'])
@login_required
def create_challenge():
    form = CreateChallengeForm()
    if form.validate_on_submit():
        #Creates a random join code
        code = createCode()
        
        #If random code is already used keep looping until it finds one that is not used
        while Challenge.query.filter_by(joincode=code).first() != None:
            code = createCode()
        
        #Create a new challenge with the random code
        #TODO: Currently, we are allowing for individuals to make challenges with the same name, we should fix this when we have the user logged in
        newChallenge = Challenge(joincode=code, open=False, host_id=current_user.get_host_id(), title=form.title.data)
        
        # Scan through all prompts and append them if there is text
        for promptForm in form.prompts.data:
            if promptForm["prompt"] is not None:
                promptText = promptForm["prompt"].strip()
                while "  " in promptText:
                    promptText = promptText.replace("  ", " ")
                prompt = Prompt(text=promptText)
                newChallenge.prompts.append(prompt)

        print("Created Challenge: Room Code {}".format(newChallenge.joincode))
        db.session.add(newChallenge)
        db.session.commit()
        #TODO: Consider whether flash messages are desire or needed at all.
        #flash('Challenge created!')
        return redirect(url_for('host.view_challenges'))
    return render_template('createChallenge.html', challengeForm = form)

@host_routes.route('/aggregate_results/<joinCode>', methods=['GET'])
@login_required
def aggregate_results(joinCode):
    results = Challenge.query.filter_by(joincode = joinCode).first().results
    listResults = list(results)
    listResults.sort(key = lambda x: x.wpm, reverse=True)
    avgWpm = 0
    avgMistakes = 0
    for result in listResults:
        avgWpm += result.wpm
        avgMistakes += result.incorrect
    if len(listResults) > 0:
        avgWpm /= len(listResults)
        avgMistakes /= len(listResults)
    #filter to top 10
    listResults = listResults[:10]
    return render_template('aggregateResults.html', results = listResults, avgWpm = round(avgWpm,1), avgMistakes = round(avgMistakes, 0))