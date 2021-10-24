from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app.Model.models import Host
from app import db
from config import Config
from app.Controller.forms import ChallengeForm, RegistrationForm

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'

@bp_routes.route('/', methods=['GET', 'POST'])
@bp_routes.route('/index', methods=['GET', 'POST'])
def index():
    challengeForm = ChallengeForm()
    hostForm = RegistrationForm()
    if challengeForm.validate_on_submit():
        print(challengeForm.title.data)
        redirect(url_for('routes.index'))

    if hostForm.validate_on_submit():
        newHost = Host(username=hostForm.username.data)
        newHost.set_password(hostForm.password.data)
        db.session.add(newHost)
        db.session.commit()
    return render_template('index.html', challengeform=challengeForm, hostform=hostForm)
    

