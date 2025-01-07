from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

# Load environment variables from the .env file
load_dotenv()

# Retrieve the username and password from environment variables
username = os.getenv("MONGO_DB_USERNAME")
password = os.getenv("MONGO_DB_PASSWORD")

# Ensure the username and password are loaded
if not username or not password:
    raise ValueError("Username or password not found in environment variables. Check your .env file.")

# URL-encode the username and password
username = quote_plus(username)
password = quote_plus(password)

# Retrieve the base MongoDB URI and substitute the encoded credentials
uri = os.getenv("MONGO_DB_URL").format(username=username, password=password)

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"An error occurred: {e}")
