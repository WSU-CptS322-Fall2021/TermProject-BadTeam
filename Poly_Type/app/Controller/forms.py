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

from app.Model.models import Prompt

class PromptForm(Form):
    prompt = TextAreaField('Prompt', [Length(min=1, max=3000)])

class CreateChallengeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    prompts = FieldList(FormField(PromptForm), min_entries=5, max_entries=5)
    submit = SubmitField('Post')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Host.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('The username already exists! Please use a different username')

class TakeChallengeForm(FlaskForm):
        username = StringField('Username', validators=[Length(min=3, max=100)])
        joincode = StringField('Join Code', validators=[Length(min=6, max=6)])
        submit = SubmitField('Join')



