from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    published = db.Column(db.String())
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False) 
    category = db.relationship('Category', backref=db.backref('books', lazy='dynamic'))

    def __init__(self, name, author, published,category_id):
        self.name = name
        self.author = author
        self.published = published
        self.category_id = category_id

    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'author': self.author,
            'published':self.published,
            'category_id': self.category_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return '<id {}>'.format(self.id)

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return '<id {}>'.format(self.id)

class CategorySchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
