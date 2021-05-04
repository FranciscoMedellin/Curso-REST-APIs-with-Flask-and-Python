from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# POST -- used to receive data
# GET -- used to send data back only

# POST /store data: {name:}
@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>',methods = ['GET']) #'http://127.0.0.1:5000/store/some_name' , get name store
def get_store(name):
    # Iterate over stores
    # If the store name matches, return it
    # If none match, return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store) # store its a is a dicctionarie
    return jsonify({'message':'store not found'})

# GET /store
@app.route('/store', methods = ['GET']) #get all names stores
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name: , price}
@app.route('/store/<string:name>/item/',methods = ['POST'])  #create item in a specific store
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : request_data["name"],
                'price' : request_data["price"]
            }
            store['items'].append(new_item)
            return jsonify({'items':store['items']})
    return jsonify({'message':'Error store not found'})

# GET /store/<string:name</item
@app.route('/store/<string:name>/item',methods = ['GET']) # all the items in a specific store
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items' : store['items']})
    return jsonify({"message":'Store not found'})

app.run(port = 5000)