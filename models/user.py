import sqlite3
from config import db

class UserModel(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String)

    def __init__(self,username,password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()

    @classmethod     
    def find_by_id(cls,id):
       return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    
