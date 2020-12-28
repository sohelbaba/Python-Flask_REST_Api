import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):

    parse = reqparse.RequestParser()
    parse.add_argument('username',type=str,required=True,help="Username is required")
    parse.add_argument('password',type=str,required=True,help="Password is required")

    def post(self):
        data = UserRegister.parse.parse_args()       

        if UserModel.find_by_username(data['username']):
            return {"message":"user already exists"}

        item = UserModel(data['username'],data['password'])
        item.save_to_db()
        
        return {"message" : "User Register Successful..."}

