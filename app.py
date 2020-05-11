from flask import Blueprint
from flask_restful import Api
from resource.book import BooksApi
from resource.Category import CategoryResource
from resource.User import UserResource
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(BooksApi, '/books')
api.add_resource(CategoryResource, '/Category')
#api.add_resource(BooksApi,'/books/<id>')
api.add_resource(UserResource,'/User')