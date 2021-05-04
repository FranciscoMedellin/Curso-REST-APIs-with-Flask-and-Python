from flask import Flask , request
from flask_restful import Resource, Api
from flask_jwt import JWT

app = Flask(__name__)
api = Api(app)

jwt = JWT(app, au)

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None) #next function give us the first item matched
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None)  is not None:
            return {"message": "An item with name {} already exists".format(name)}, 400 #bad request code

        data = request.get_json(silent=True)
        item = { "name": name, 'price': data["price"]}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)

