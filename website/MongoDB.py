from pymongo import MongoClient



def get_connection():
    #uri="mongodb+srv://pedroguillferri9:tyu9eLgtAYDlU3ue@cluster0.fjkmsms.mongodb.net/"
    #client = MongoClient(uri)
    client = MongoClient('192.168.0.29',27017)
    
    try:
        client.admin.command('ping')
        print("Estas Conectado a MongoDB")
    except Exception as e:
        print(e)
    db = client.Web
    return db