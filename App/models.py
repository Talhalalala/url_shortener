import string
from datetime import datetime
from random import choices
from sqlalchemy.sql import func
from .extensions import db


class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(1000))
    shortened_url = db.Column(db.String(5), unique=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shortened_url = self.shortner()

    def shortener(self):
        char = string.ascii_letters + string.digits
        shortened_url = ''.join(choices(char, k=5))

        link = self.query.filter_by(shortened_url=shortened_url).first()

        if link:
            return self.shortener()

        return shortened_url





