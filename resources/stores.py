from flask_restful import Resource,reqparse
from config import db
from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):

    @jwt_required()
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        
        return {"message" : "specific store not found.."}

    def post(self,name):
        store = StoreModel(name)
        store.save_to_db()
        return {"message" : "StoreCreated.."}

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        else:
            return {"message" : "store not found"}
        
        return {"message" : "Store Deleted.."}


class StoreList(Resource):
    def get(self):
        return {"stores" : [store.json() for store in StoreModel.query.all()]}
