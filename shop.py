from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/<nomber>')
def greeting(nomber):
    return render_template('front.html' , nomber=nomber)

@app.route('/shop')
def shop_front_view():
    products = [
        {
            "name": "Dog Shampoo",
            "brand": "Top Fin",
            "price": 14.24,
            "stock": 15
        },
             {
            "name": "Cat Shampoo",
            "brand": "Top Fin",
            "price": 14.24,
            "stock": 15
        },
             {
            "name": "Dog Medecine",
            "brand": "Top Fin",
            "price": 14.24,
            "stock": 15
        },
             {
            "name": "Dog Medecine",
            "brand": "Top Fin",
            "price": 14.24,
            "stock": 15,
            "image": "https://cdn0.woolworths.media/content/wowproductimages/large/892654.jpg"
         },
    ]   
    for product in products:
        print(product['name'])

    return render_template('shopfront.html' , products=products)

