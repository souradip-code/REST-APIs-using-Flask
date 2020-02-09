from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT
from db import db

from security import authenticate, identity

from resources.item import Item, ItemList
from resources.user import UserRegister, UserList
from resources.store import StoreList, Store

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.secret_key = 'souradip'
api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()

jwt = JWT(app,authenticate,identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(UserList, '/registered_users')


if __name__=='__main__':
    db.init_app(app)
    app.run(port=5000,debug=True)