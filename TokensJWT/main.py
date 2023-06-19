from flask import Flask
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
import jwt


class User(Resource):

    # /usuarios/{user_id}
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404  # not found.