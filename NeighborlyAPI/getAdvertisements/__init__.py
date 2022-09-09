import azure.functions as func
import pymongo
import json
import os
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = os.getenv("MONGO_CONNECTION_STRING", "")
        client = pymongo.MongoClient(url)
        database = client[os.getenv("MONGO_DB_NAME", "")]
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

