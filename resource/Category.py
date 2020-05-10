from flask import request
from flask_restful import Resource
import sys
sys.path.append('..')
from models import Category, CategorySchema
from flask import Blueprint, Response, request,jsonify

categories_schema = CategorySchema(many=True)
category_schema = CategorySchema()

class CategoryResource(Resource):
    def get(self):
        categories = Category.query.all()
        #categories = categories_schema.dump(categories).data
        return jsonify([e.serialize() for e in categories])
        # return {'status': 'success', 'data': categories}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data = category_schema.load(json_data)
        print(data)
        # if errors:
        #     return errors, 422
        category = Category.query.filter_by(name=data['name']).first()
        if category:
            return {'message' : 'Category already exists'}, 400
        category = Category(
            name=json_data['name']
        )
        category.save()
        result = category_schema.dump(category)

        return {"status": 'success','data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data = category_schema.load(json_data)
        # if errors:
        #     return errors, 422
        category = Category.query.filter_by(id=data[id]).first()
        if not category:
            return {'message':'Category does not exist'}, 400
        category.name = data['name']
        category.save()
        result = category_schema.dump(category).data
        
        return {"status": 'success', 'data':result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = category_schema.load(json_data)
        if errors:
            return errors, 422

        category = Category.query.filter_by(id=data['id'])
        category.delete()
        result = category_schema.dump(category).data

        return {"status": 'sucess', 'data': result}, 204

