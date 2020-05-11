from flask_restful import Resource
import sys
sys.path.append('..')
from models import UserModel, UserSchema
from flask import Blueprint, Response, jsonify, request

user_schema = UserSchema()

class UserResource(Resource):
    def get(self):
        users = UserModel.query.all()
        return jsonify([user.serialize() for user in users])

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data = user_schema.load(json_data)
        user = UserModel.query.filter_by(name=data['email']).first()
        if user:
            return {'message': 'user email already exists'}, 400
        new_user = UserModel(
            name=json_data['name'],
            email = json_data['email'],
            password = json_data['password']
        )
        new_user.save()
        result = user_schema.dump(new_user)

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        
        data = user_schema.load(json_data)
        user = UserModel.query.filter_by(id=data[id]).first()
        if not user:
            return {'message': 'Category does not exist'}, 400
        user.name = data['name']
        user.save()
        result = user_schema.dump(UserModel).data

        return {"status": 'success', 'data': result}, 204
        


