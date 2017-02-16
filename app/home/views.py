from flask import render_template, abort, request,flash
from flask_login import login_required, current_user
from sqlalchemy import and_
from . import home
from ..models import UserBook, Book
from .. import db
from datetime import datetime,timedelta





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
def books():
	return render_template('home/allbooks.html', title="All Books")

@home.route('/borrow_book', methods=['POST'])
def borrow_books():
	# Save borrowed book
	user_id = current_user.id
	books = get_user_borrowed_books(user_id)

	borrow_date = timestamp = datetime.now()
	return_date = borrow_date + timedelta(10)
	book_id = request.form['book_id']

	if book_id:
		add_user_book = True

		books = get_user_borrowed_books(user_id)
		no_of_books = books.count()
		return_date = return_date.strftime("%d-%m-%y")
		borrow_date = borrow_date.strftime("%d-%m-%y")

		user_book = UserBook(user_id = user_id, book_id = book_id, borrow_date = borrow_date, return_date = return_date)
		try:
			if book_is_borrowed(user_id, book_id):
				#check if owner has book already
				flash("You have already Borrowed this Book, Please return it first :)")
			else:		
				#go ahead and allow user to borrow book
				db.session.add(user_book)
				db.session.commit()
				flash("Successfully Borrowed book, wait for approval from admin",'success')

		except:
			flash("You have borrowed this book already!")
		

	return render_template('home/borrowed_books.html', get_dates = get_dates, books = books, title="Borrow Books")

@home.route('/borrowed_books', methods = ['GET', 'POST'])
@login_required
def list_borrowed_books():
	user_id = current_user.id

	books = UserBook.query.get(user_id)
	if not books:
		books = None

	return render_template('home/borrowed_books.html',  books = books, title="Borrowed Books")
	


def book_is_borrowed(user_id, book_id):
	return UserBook.query.filter(UserBook.user_id==user_id).filter(UserBook.book_id==book_id).first()

def get_user_borrowed_books(user_id):
	# return UserBook.query.join(Book, UserBook.books_id==books.id).filter(UserBook.user_id==request.form['user_id'])
	return Book.query.join(UserBook, Book.id==UserBook.book_id).filter(UserBook.user_id==user_id)

def get_dates(user_id, book_id):
	dates = UserBook.query.filter(user_id == user_id, book_id == book_id).first()
	# raise
	return dates

	

	