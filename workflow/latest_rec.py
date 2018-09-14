import pymongo
import pprint

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['Workflow']
collection = database['reportdownload_deal']


#Get the 'DealID' latest record from the collection
def get_latest_record_id_from_db():
    record = list(collection.find({}).sort("DealID", pymongo.DESCENDING).limit(1))
    return record[0]['DealID']


#insert new record via increase 'DealID' +1 and give your new 'ShortName'
def insert_record(shortname):
    try:
        latest_id = get_latest_record_id_from_db()
        f = collection.insert({'DealID': latest_id + 1, 'ShortName': shortname})
    except Exception as e:
        e = e
    return f


user_input = input('Write ShortName of the company:')

# insert 'ShortName' record whatever you want
insert_record(user_input)






