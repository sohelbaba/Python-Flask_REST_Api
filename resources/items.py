from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from flask import jsonify
from models.item import ItemModel


class Item(Resource):
    
    parse = reqparse.RequestParser()
    parse.add_argument('name',type=str,required=True,help="name required")
    parse.add_argument('price',type=float,required=True,help="price required")
    parse.add_argument('store_id',type=int,required=True,help="store id required")
    

    @jwt_required()
    def get(self,name):

        item = ItemModel.find_by_name(name)
        if item:
            return item.json()

        return {"message" : "requested Item is not Found"},401

    def post(self,name):

        if ItemModel.find_by_name(name):
            return {"message" : "already exists"}

        data = Item.parse.parse_args()  
        item = ItemModel(name,data['price'],data['store_id'])    
        try:
            item.save_to_db()
        except:
            return {"message" : "Error :: Inserting data"},500 # 500 : server error

        return item.json()

    def delete(self,name):

        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {"message" : "Item deleted"}
    
    def put(self,name):
        
        item = ItemModel.find_by_name(name) #fetch item if you have 
        data = Item.parse.parse_args()  # updated data come from request

        if item:
            item.price = data['price']
        else:
            item = ItemModel(name,data['price'],data['store_id'])  #if not then create item 
        
        item.save_to_db()
        return item.json()
            

class List(Resource):
    
    def get(self):
        return {"item" : [item.json() for item in ItemModel.query.all()]}