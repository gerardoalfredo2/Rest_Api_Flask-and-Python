

from flask import Flask,jsonify,request, render_template

app=Flask(__name__)
stores=[
    {
     'name':'My wonderful store',
     'items':[
         {
             'name':'my_item',
             'price':15.99
             }
         ]
        }
    ]

@app.route('/')
def home():
    return render_template('index.html')
#Post :-used to receive data
#Get  :-Used to send data back only

#Post:/store data:{name:}
@app.route('/store',methods =['POST'])
def create_store():
    request_data=request.get_json()
    new_store={
        'name':request_data['name'],
        'items':[]}
    stores.append(new_store)
    return jsonify(new_store)
#Get /store/<string:name>
@app.route('/store/<string:name>')  #'http://127.0.0.1:5000/store/store_name'
def get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
        return jsonify({'message':'store not found'})
    #Iterate over Stores
    #if the store name matches, return it
    #If none match, return an error message

    
#Get:/store
@app.route('/store')  #
def get_stores():
    return jsonify({'stores':stores})
#Post /store/<string:name>/item<name:,price:>
@app.route('/store/<string:name>/item',methods =['POST'])
def create_item_in_store(name):
   request_data=request.get_json()
   for store in stores:
       if store['name']==name:
           new_item={
               'name':request_data['name'],
               'price':request_data['price']
               }
           store['items'].append(new_item)
           return jsonify(new_item)
   return jsonify({'message':'store not found'})
    
#Get /store/<string:name>/item
@app.route('/store/<string:name>/item')  #
def get_items_in_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})
    return  jsonify({'message':'store not found'})
app.run(port=5000)