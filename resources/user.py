import sqlite3
from flask_restful import Resource, reqparse

from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required = True,
        help = 'This field cannot be empty'
    )
    parser.add_argument('password',
        type=str,
        required = True,
        help = 'This field cannot be empty'    
    
    )
    


    def post(self):
        data = UserRegister.parser.parse_args()
        print('---------',data)

        if UserModel.find_by_username(data['username']):
            return {'message': 'UserName already exists'},400
        
        user = UserModel(data.username,data.password)
        user.saveuser_to_db()

        return {'message': 'User registration successful'},201



class UserList(Resource):
    # @jwt_required()
    def get(self):
        print('Inside Get')
        allUsers =  UserModel.query.all()
        
        return {'Users':list(map(lambda user :user.json(),allUsers))}