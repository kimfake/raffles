from flask.ext.wtf import Form
from wtforms import validators, IntegerField
from wtforms.fields.html5 import EmailField

class RaffleForm(Form):
    email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
    raffle_count = IntegerField('Raffle count', default=1)
