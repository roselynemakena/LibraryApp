from flask import flash,redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from . forms import LoginForm, RegistrationForm
from .. import db
from ..models import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
	'''
	adds register route to enable a user to login
	'''

	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email = form.email.data,
					username = form.username.data,
					password = form.password.data
				)

		#add username to the database
		db.session.add(user)
		db.session.commit()
		flash("you have successfully signed up!")


		#redirect to login page
		return redirect(url_for("auth.login"))
	return render_template('auth/register.html', form=form, title='Register User')


@auth.route('/login', methods=['GET', 'POST'])
def login():
	form=LoginForm()

	if form.validate_on_submit():
		#check user exists in database
		user = User.query.filter_by(email=form.email.data).first()

		if user is not None and user.verify_password(form.password.data):
			login_user(user)
			if user.is_admin:
				return redirect(url_for('home.admin_dashboard'))
			else:
				return redirect(url_for('home.dashboard'))
		else:
			flash("Wrong Password yo!")
	#if user does not exist on database
	return render_template('auth/login.html', form=form, title="Login")

@auth.route('/logout')
@login_required
def logout():
	logout_user()

	flash("You have successfully logged out")

	return redirect(url_for('auth.login'))
