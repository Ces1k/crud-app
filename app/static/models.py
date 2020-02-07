from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Author(db.Model):
    __tablename__ = "author"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    books = relationship("Book", backref="author")

    def __repr__(self):
        return f"{self.name}"


class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('author.id'))
    # author = relationship(Author)

    def __repr__(self):
        return f"{self.title}"
