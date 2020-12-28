from flask import Flask
from flask_restful import Api,Resource
from flask_jwt import JWT,jwt_required

from resources.items import Item,List
from resources.user import UserRegister
from resources.stores import Store,StoreList
from security import authentication,identity


app = Flask(__name__)
app.secret_key = 'secure'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'

@app.before_first_request
def create_table():
    db.create_all()


jwt = JWT(app,authentication,identity)
api = Api(app)

api.add_resource(Item,'/item/<string:name>')
api.add_resource(List,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')


if __name__ == '__main__':
    from config import db
    db.init_app(app)
    app.run(port=5000)