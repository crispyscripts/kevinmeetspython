from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

adminConnectionString = 'mongodb+srv://crisp:***@kevin-8xfyp.azure.mongodb.net/test?retryWrites=true&w=majority'

client = MongoClient(adminConnectionString)
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)


