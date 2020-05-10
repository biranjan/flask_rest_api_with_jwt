from flask_sqlalchemy import SQLAlchemy

# initialize db
db = SQLAlchemy()

from .BookModel import Book, Category, CategorySchema