from flask import render_template, abort
from flask_login import login_required, current_user
from . import home




@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
	if not current_user.is_admin:
		abort(403)
	return render_template('home/admin_dashboard.html', title="Admin Dashboard")


@home.route('/')
def homepage():
	'''
		Homepage for home
	'''
	return render_template('home/index.html', title="Homepage")

@home.route('/dashboard')
def dashboard():
	'''
		Homepage for home
	'''
	return render_template('home/dashboard.html', title="Dashboard")
@home.route('/allbooks')
def allbooks():
	return render_template('home/allbooks.html', title="All Books")
	