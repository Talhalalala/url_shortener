from flask import Blueprint, redirect, render_template, request, flash, jsonify

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return '<h1>This is the homepage</h1>'
