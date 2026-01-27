from collections.abc import MutableMapping
from collections import namedtuple
from pymongo import MongoClient # type: ignore


uri="mongodb+srv://root:MADhav44@collage.qvvopgb.mongodb.net/?appName=Collage"


## Create a new client and connect to the server 
client=MongoClient(uri)

## Send a ping to confirm a successful connection 
try:
    
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)