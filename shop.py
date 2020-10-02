from flask import Flask
from flask import render_template
app = Flask(__name__)
import pymongo

client = pymongo.MongoClient("mongodb+srv://francees:Blackberrypriv1@cluster0.bnodg.mongodb.net/easywebshop?retryWrites=true&w=majority")
db = client.easywebshop
product_collection = db.products


@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/<nomber>')
def greeting(nomber):
    return render_template('front.html' , nomber=nomber)

@app.route('/shop')
def shop_front_view():
    products = product_collection.find()
    


    return render_template('shopfront.html' , products=products)

