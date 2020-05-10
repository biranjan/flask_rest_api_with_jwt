from flask import Blueprint, Response, request,jsonify
from models import Book
from flask_restful import Resource


class BooksApi(Resource):
    def get(self):
        books = Book.query.all()
        return jsonify([e.serialize() for e in books])

    def post(self):
        name = request.args.get('name')        
        author = request.args.get('author')
        published = request.args.get('published')
        category_id = request.args.get('category_id')

        try:
            book = Book(name=name,author=author,published=published,category_id=category_id)
            book.save()
            return "Book added. book id={}".format(book.id)
        except Exception as e:
            return(str(e))

    def get_by_id(self,id):
        book = Book.query.filter_by(id=id).first()
        return jsonify(book.serialize())

def initializeRoutes(api_=BooksApi()):
    from .book import BooksApi
    api_.add_resource(BooksApi, '/books')
    api_.add_resource(BooksApi,'/books/<id>')


#books = Blueprint('books', __name__)

# @books.route("/")
# def hello():
#     return "Hello World"

# @books.route("/add", methods=['POST'])
# def add_book():
#     name = request.args.get('name')
#     author = request.args.get('author')
#     published = request.args.get('published')
#     try:
#         book = Book(
#             name=name,
#             author=author,
#             published=published
#         )
#         db.session.add(book)
#         db.session.commit()
#         return "Book added. book id={}".format(book.id)
#     except Exception as  e:
#         return(str(e))

# @books.route("/getall")
# def get_all():
#     try:
#         books=Book.query.all()
#         return jsonify([e.serialize() for e in books])
#     except Exception as e:
#         return(str(e))

# @books.route("/get/<id>")
# def get_by_id(id):
#     try:
#         book = Book.query.filter_by(id=id).first()
#         return jsonify(book.serialize())
#     except Exception as e:
#         return(str(e))
