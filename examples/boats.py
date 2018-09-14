import pymongo
from bson.son import SON
from mongoengine import *
import mongoengine as me

uri =  "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['boats']
collection = database['sailingboats']

# sailingboats = collection.insert_many([{
#     "product" : "benetaou",
#     "feat" : 40.75,
#     "type" : "race"
# },
# {
#
#     "product" : "delphia",
#     "total" : 10.75,
#     "customer" : "race"
# },
# {    "product" : "oceanis",
#     "feat" : 20.50,
#     "type" : "entertainment"
# },
# {
#
#     "product" : "delphia",
#     "total" : 25.75,
#     "customer" : "entertainment"
# },
# {    "product" : "benetaou",
#     "feat" : 38.75,
#     "type" : "race"
# },
# {
#
#     "product" : "oceanis",
#     "total" : 112.75,
#     "customer" : "entartainment"
# }
# ])


# sailingboats = collection.update({"product": "delphia"},
#                                  {"product": "delphia32",
#                                   "total": 32,
#                                   "type": "race"})
#
# sailingboats = collection.find({})
# for sailingboat in sailingboats:
#     print(sailingboat)



# pipeline = [{"$unwind" :"$product" },
#             {"$group" : {"_id":"$product","count" : {"$sum": 1}}},
#             {"$sort": SON([("count", -1),("_id" , -1)])}]
# import pprint
# pprint.pprint(list(collection.aggregate(pipeline)))

me.connect("examples")

class Boat(Document):
    product=StringField()
    total=FloatField()
    customer=StringField(max_length=20000)


b = Boat(total=1995).save()
a = Boat(total=1996).save()

#
# p= Boat.objects(total__gte =1994)
# print(p)
#
# a=Boat.objects(total=1995)
# print(a)

q=b.delete(total=1995)
