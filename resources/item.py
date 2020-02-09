from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
import sqlite3
from models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type= float,
            required = True,
            help = 'This is cannot be empty'
    )
    parser.add_argument('store_id',
            type= int,
            required = True,
            help = 'This is cannot be empty'
    )
    @jwt_required()
    def get(self,name):
     
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'item not found'}




    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message': f'item with the name {name} is already exist'},400

        request_data = Item.parser.parse_args()
        item =ItemModel(name,request_data['price'],request_data['store_id'])

        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'},500

        return item.json(),201


    def delete(self,name):
        item = ItemModel.find_by_name(name)

        if item:
            item.delete_from_db()
        
        return {'message':'Item Deleted!!!'}

    def put(self,name):
       
        request_data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        print('+++++++',request_data)
        print('-------',item)
        if item:
            item.price = request_data['price']  
        else:
            item = ItemModel(name, request_data['price'],request_data['store_id'])
            
        item.save_to_db()
        return item.json()  



class ItemList(Resource):
    @jwt_required()
    def get(self):
        allItems =  ItemModel.query.all()
        # print('------',allItems)
        return {'items':list(map(lambda item :item.json(),allItems))}