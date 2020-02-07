from app import app
from app import db
from flask import render_template
from flask import redirect
from flask import request
from app.static.models import Author
from app.static.models import Book


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # Gather a new data
        author = request.form['author']
        book = request.form['title']
        # Process the data
        new_author = Author(name=author)
        new_book = Book(title=book, author_id=new_author.id)
        new_author.books.append(new_book)
        try:
            db.session.add(new_author)
            db.session.add(new_book)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return e
    else:
        authors = Author.query.order_by(Author.id).all()
        return render_template('index.html', authors=authors)


@app.route('/authors')
def authors():
    authors = Author.query.order_by(Author.id).all()
    return render_template('authors.html', authors=authors)


@app.route('/books')
def books():
    books = Book.query.order_by(Book.id).all()
    return render_template('books.html', books=books)
