
#import pprint
import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['DemoDB1']
collection = database['purchase_orders']




purchase_orders = collection.insert([{
    "product" : "ymuyuy",
    "total" : 4.75,
    "customer" : "Miyke"
},
{

    "product" : "lemon",
    "total" : 5.75,
    "customer" : "Lemoda"
}]

)

purchase_orders = collection.find({})


for purchase_order in purchase_orders:
    #pprint.pprint(purchase_order)
    print(purchase_order)

purchase_orders = collection.count()
print(purchase_orders)

t = 8.2
for purchase in collection.find({"total" : {"$gte": t}}).sort("customer"):
    print(purchase)

#
# class Product:
#     product: int
#     total: float
#     customer: str
#
# Product.objects(__raw__={
#     "product" : "ymuyuy",
#     "total" : 4.75,
#     "customer" : "Miyke"
# }).first()
# p = Product()
#
# p.total = 5333
# p.save()


import mongoengine as me

me.connect('users')


class User(me.Document):
    id = me.IntField()
    name = me.StringField(20, unique=True)


ali = User(name='Alil')
ali.save()

User.objects(name='Ali')
User.objects.find()