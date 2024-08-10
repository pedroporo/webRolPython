from pymongo import MongoClient



def get_connection():
    client = MongoClient('192.168.0.29',27017)
    db = client.Web
    return db