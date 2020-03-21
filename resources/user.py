import sqlite3
from flask_restful import Resource, reqparse

from models.user import UserModel
    
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help='Username is required'
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help='Password is required'
    )
    
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}, 400
        
        user = UserModel(**data)
        
        try:
            user.save_to_db()
        except:
            return {'message': 'An error occurred while registering the user'}, 500
        
        return {'message': 'User created successfully!'}, 201
        