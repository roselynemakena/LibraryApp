from  flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


from ..models import Book

class BookForm(FlaskForm):
	'''
	Add books and edit books
	'''
	title = StringField('Title', validators = [DataRequired()])
	description = StringField('Description', validators = [DataRequired()])
	submit = SubmitField('Add Book')