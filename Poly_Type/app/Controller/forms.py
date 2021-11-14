from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, BooleanField, Form
from wtforms.fields.core import FieldList, FormField
from wtforms.fields.simple import PasswordField
from wtforms.validators import  DataRequired, EqualTo, Length, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, BooleanField
from wtforms.validators import  DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from app.Model.models import Host
from flask_login import current_user


from app.Model.models import Prompt

class PromptForm(FlaskForm):
    prompt = TextAreaField('Prompt', [Length(min=0, max=3000)])

class CreateChallengeForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    prompts = FieldList(FormField(PromptForm), min_entries=5, max_entries=5)
    submit = SubmitField('Post')

class RegistrationForm(FlaskForm):
    reg_username = StringField('Username', validators=[DataRequired()])
    reg_password = PasswordField('Password', validators=[DataRequired()])
    reg_password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('reg_password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Host.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('The username already exists! Please use a different username')

class UpdateInfoForm(FlaskForm):
    def validate_username_update(self, username):
        user = Host.query.filter_by(username=username.data).first()
        print(current_user.username)
        if user is not None and user.username != current_user.username: #Check to see if name is already used and not current_user's username
                raise ValidationError('The username already exists! Please use a different username')

    reg_username = StringField('Username', validators=[DataRequired(), validate_username_update])
    reg_password = PasswordField('Password', validators=[DataRequired()])
    reg_password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('reg_password')])
    submit = SubmitField('Update')



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class JoinChallengeForm(FlaskForm):
    nickname = StringField('Nickname', validators=[Length(min=3, max=100)])
    joincode = StringField('Join Code', validators=[Length(min=6, max=6)])
    submit = SubmitField('Join')



