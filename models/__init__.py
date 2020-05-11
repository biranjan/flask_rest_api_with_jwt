from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize db
db = SQLAlchemy()
bcrypt = Bcrypt()
from .BookModel import Book, Category, CategorySchema
from .UserModel import UserModel, UserSchema
