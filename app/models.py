from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


from app import db, lm

class User(UserMixin, db.Model):
	'''
	Create User Table
	'''

	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(50),index=True, unique=True)
	username = db.Column(db.String(50),index=True, unique=True)
	password = db.Column(db.String(128))
	password_hash = db.Column(db.String(128))
	is_admin = db.Column(db.Boolean, default=False)


	@property
	def password():
		'''
		prevent password from being accessed
		'''	
		raiseAttributeError('Password is not readable!')

	@password.setter
	def password(self, password):
		'''
			make password hashed
		'''

		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		'''
			check passwords if matching
		'''

		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<User: {} >'.format(self.username)


	@lm.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))


class Book(db.Model):
	'''
	Create book table
	'''
	__tablename__ = 'books'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	description = db.Column(db.String(500))
	# created_by = db.Column(db.Integer, db.ForeignKey('users.id'), default=1)
	# users = db.relationship('User', backref='book', lazy='dynamic')

	def __repr__():
		return 'Book: {}'.format(self.book_title)

	def load_book():
		return Book.query.get(int(book_id))


			

