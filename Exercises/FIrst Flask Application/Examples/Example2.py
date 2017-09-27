from flask import Flask,jsonify

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


#Post :-used to receive data
#Get  :-Used to send data back only

#Post:/store data:{name:}
@app.route('/store',methods =['POST'])
def create_store():
    pass
#Get /store/<string:name>
@app.route('/store/<string:name>')  #'http://127.0.0.1:5000/store/store_name'
def get_store(name):
    pass
#Get:/store
@app.route('/store')  #
def get_stores():
    return jsonify({'stores':stores})
#Post /store/<string:name>/item<name:,price:>
@app.route('/store/<string:name>/item',methods =['POST'])
def create_item_in_store(name):
    pass
#Get /store/<string:name>/item
@app.route('/store/<string:name>/item')  #
def get_items_in_store(name):
    pass
app.run(port=5000)