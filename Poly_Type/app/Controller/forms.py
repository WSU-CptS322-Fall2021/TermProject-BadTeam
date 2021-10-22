from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, BooleanField, Form
from wtforms.fields.core import FieldList, FormField
from wtforms.validators import  DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, BooleanField
from wtforms.validators import  DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput

from app.Model.models import Prompt

class PromptForm(Form):
    prompt = TextAreaField('Prompt', [Length(min=1, max=3000)])

class ChallengeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    prompts = FieldList(FormField(PromptForm), min_entries=5, max_entries=5)
    submit = SubmitField('Post')

