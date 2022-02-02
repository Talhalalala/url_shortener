from flask import Blueprint, redirect, render_template, request, flash, jsonify
from .extensions import db
import json
from werkzeug import exceptions
import shortuuid
from .models import Urls, find_url, find_short, Form




views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    form = Form()
    print(form)
    if request.method == 'POST':
        if find_url(form.url.data):
            link = find_url(form.url.data).url
            short = find_url(form.url.data).shortened_url
            return render_template('new_link.html', url=link, shortened_url=short)
        else:
            short = shortuuid.uuid()[:5]
            url = Urls(url=form.url.data, shortned_url=short)
            db.session.add(url)
            db.session.commit()
            return render_template('home.html', url=url.url, shortened_url=short)
    else:
        return render_template('home.html', title ='home')
    

@views.route('/new_link', methods = ['POST'])
def new_link():
    url = request.form.get('url')
    link = Urls(url=url)
    db.session.add(link)
    db.session.commit()

    return render_template('new_link.html', new_link = link.shortened_url, url=link.url, title='new_link')

@views.route('/<shortened_url>')
def to_new_link(shortened_url):
    link = Urls.query.filter_by(shortened_url=shortened_url).first_or_404()
    return redirect(link.url)


@views.errorhandler(exceptions.NotFound)
def handle_404(err):
    return render_template('errors/404.html'), 404

@views.errorhandler(exceptions.BadRequest)
def handle_405(err):
    return render_template('errors/405.html'), 405


@views.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return render_template('errors/500.html'), 500