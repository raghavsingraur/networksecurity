import os 
import sys
import json
from dotenv import load_dotenv

# Call load_dotenv() to load environment variables from the .env file
load_dotenv()

# Retrieve the MongoDB URL from the environment variables
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)
