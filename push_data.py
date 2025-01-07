from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

# Encode the username and password
username = quote_plus("kuwarraghvendrasingh")
password = quote_plus("Raghav@iitian25")

# Construct the URI with the encoded username and password
uri = f"mongodb+srv://{username}:{password}@cluster0.qtcip.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
