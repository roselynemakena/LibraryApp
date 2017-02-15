from flask import abort, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_required

from . import admin
from . forms import BookForm
from .. import db
from ..models import Book, User, UserBook




def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


@admin.route('/books', methods=['GET', 'POST'])
@login_required
def list_books():
    """
    List all departments
    """
    # check_admin()
    books = Book.query.all()

    return render_template('admin/books/books.html', books=books, title="Books")


@admin.route('/books/add', methods=['GET', 'POST'])
@login_required
def add_book():
		check_admin()

		add_book = True

		form = BookForm()

		if form.validate_on_submit():
			book = Book(title = form.title.data,
						description = form.description.data
						)
			try:
				db.session.add(book)
				db.session.commit()
				flash("Successfully added Book")
			except:
				flash("Book already added")

			return redirect(url_for('admin.list_books'))
		return render_template('admin/books/book.html', action = "Add", add_book = add_book,form=form,title="Add Book")


@admin.route('/books/edit/<int:id>', methods=['POST', 'GET'])
@login_required
def edit_book(id):
	check_admin()

	add_book = False

	book=Book.query.get_or_404(id)
	form = BookForm(obj = book)

	if form.validate_on_submit():

		book.title = form.title.data
		book.description = form.description.data

		db.session.commit()

		flash("Book edited successfully!!")

		return redirect(url_for('admin.list_books'))


	form.title.data = book.title
	form.description.data = book.description
	return render_template('admin/books/book.html', action="Edit", add_book=add_book, form=form,book=book,title="Edit Book")

@admin.route('/books/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_book(id):
    """
    Delete a department from the database
    """
    check_admin()

    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('You have successfully deleted the book!.')

    # redirect to the departments page
    return redirect(url_for('admin.list_books'))

    return render_template(title="Delete Book")

@admin.route('/borrowed_books')
@login_required
def borrowed_books():
	check_admin()

	users = get_all_users()
	print(users)

	return render_template('/admin/books/borrowed_books.html', users = users, title="Borrowed books")


@admin.route('/user_books', methods=['POST'])
@login_required
def user_books():
	check_admin()
	user_id = request.form['user_id']
	user = User.query.get(user_id)

	user_books = get_user_borrowed_books(user_id)

	print("*******************************")
	print(user_books)

	return render_template('/admin/books/user_books.html', user =user, books = user_books, title="User Borrwed Books")


def get_all_users():
	users = User.query.all()
	return users

def get_user_borrowed_books(user_id):
	user_books = Book.query.join(UserBook, Book.id == UserBook.book_id).filter(UserBook.user_id == user_id)
	return user_books






























































