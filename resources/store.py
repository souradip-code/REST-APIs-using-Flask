from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
import sqlite3
from models.store import StoreModel

class Store(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
            type = str,
            required = True,
            help = 'This is cannot be empty'
    )

    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message': f'store with the name {name} is already exist'},400
        store =StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred saving store to dv'},500
        return store.json(),201


    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message':'Store Deleted!!!'}



class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
