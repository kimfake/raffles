# define database models here
import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

def get_db_uri():
    return 'sqlite:///{}'.format(os.path.abspath('app.db'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    email = db.Column(db.String(120), unique=True)


    def __init__(self, email):
        self.email = email

    @validates
    def validate_email(self, key, address):
        assert '@' in address
        return address


    def __repr__(self):
        return '<User {0}>'.format(self.email)


class Raffle(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=True,
    )

    user = db.relationship(
        'User',
        backref=db.backref('raffles', lazy='dynamic')
    )

    colour = db.Column(db.String(120))
    
    up1 = db.Column(db.String(4))
    
    up2 = db.Column(db.String(4))

    # this ensures all the generated raffles are unique
    __table_args__ = (
        db.UniqueConstraint(
            'colour', 'up1', 'up2', name='_color_up1_up2_uc'
        ),
    )


    def __init__(self, colour, up1, up2, user_id=None):
        self.user_id = user_id
        self.colour = colour
        self.up1 = up1
        self.up2 = up2

    def __repr__(self):
        return '<Raffle {0} {1}-{2}>'.format(self.colour, self.up1, self.up2)