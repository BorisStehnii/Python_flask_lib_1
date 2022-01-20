from flask import render_template
from app import fapp


@fapp.route('/')
@fapp.route('/index')
def index():
    user = {'username': 'Boris'}
    posts = [
        {
            'author': {'username': 'Den'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Anna'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

