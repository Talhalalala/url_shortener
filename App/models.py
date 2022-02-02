import string
from random import choices
from sqlalchemy.sql import func
from .extensions import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length



class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(1000))
    shortened_url = db.Column(db.String(5), unique=True)

    def __repr__(self):
        return f"Urls('{self.url}', '{self.shortened_url}')"

def find_url(url):
    link = Urls.query.filter_by(url=url).first()
    print(link)
    return link


def find_short(shortened_url):
    link = Urls.query.filter_by(shortened_url=shortened_url).first()
    print(link)
    return link


class Form(FlaskForm):
    url = StringField('URL', validators=[DataRequired(), Length(min=5, max=250)])
    submit = SubmitField('Submit')


    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.shortened_url = self.shortener()

    # def shortener(self):
    #     char = string.ascii_letters + string.digits
    #     shortened_url = ''.join(choices(char, k=5))

    #     link = self.query.filter_by(shortened_url=shortened_url).first()

    #     if link:
    #         return self.shortener()

    #     return shortened_url





