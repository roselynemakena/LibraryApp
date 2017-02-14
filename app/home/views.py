from flask import render_template
from flask_login import login_required
from . import home


@home.route('/')
def homepage():
	'''
		Homepage for home
	'''

	return render_template('home/index.html', title="Homepage")

@home.route('/dashboard')
def dashboard():
	return render_template('home/index.html', title="Homepage")
	