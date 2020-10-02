import pymongo

client = pymongo.MongoClient("mongodb+srv://francees:Blackberrypriv1@cluster0.bnodg.mongodb.net/easywebshop?retryWrites=true&w=majority")
db = client.easywebshop
product_collection = db.products

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

result = product_collection.insert_many(products)
print(result)

