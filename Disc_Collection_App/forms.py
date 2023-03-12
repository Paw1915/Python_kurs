from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class DiscCollection(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    artist = TextAreaField('Wykonawca', validators=[DataRequired()])
    unpacked = BooleanField('W folii?')