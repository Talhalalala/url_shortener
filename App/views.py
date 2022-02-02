from flask import Blueprint, redirect, render_template, request, flash, jsonify
from .extensions import db
# import json
# from werkzeug import exceptions
from .models import Urls



views = Blueprint('views', __name__)


@views.route('/')
def home():
    # return render_template('home.html', title ='home')
    return '<h1>This is the homepage</h1>'

# @views.route('/new_link', methods = ['POST'])
# def new_link():
#     url = request.form.get('url')
#     link = Urls(url=url)
#     db.session.add(link)
#     db.session.commit()

#     return render_template('new_link.html', new_link = link.shortened_url, url=link.url)

# @views.route('/<shortened_url>')
# def to_new_link(shortened_url):
#     link = Urls.query.filter_by(shortened_url=shortened_url).first_or_404()
#     return redirect(link.url)


