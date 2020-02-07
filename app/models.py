from app import db
from sqlalchemy.orm import relationship


class Author(db.Model):
    __tablename__ = "Authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    book = relationship("Book", back_populates="parent")

    def __repr__(self):
        return f"<Author: {self.name}>"


class Book(db.Model):
    __tablename__ = "Books"

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, ForeignKey('author.id'))
    title = db.Column(db.String(100), unique=True, nullable=False)

    author = relationship("Author", back_populates="child")

    def __repr__(self):
        return f"<Title: {self.title}>"
