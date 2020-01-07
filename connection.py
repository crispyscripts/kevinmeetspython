print('Hello')

import json

user = ""
password = ""

with open("pword.json") as pwords:
    data = json.load(pwords)
    for p in data["admin"]:
        user = p["user"]
        password = p["password"]

from pymongo import MongoClient

client = MongoClient('mongodb+srv://' + user + ':' + password + '@kevin-8xfyp.azure.mongodb.net/test?retryWrites=true&w=majority')

db=client.business

serverStatusResult=db.command("serverStatus")

pprint(serverStatusResult)
