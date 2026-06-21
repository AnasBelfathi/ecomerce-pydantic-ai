"""
Database configuration and MongoDB Connection setup
"""

from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load Envirionment variables from .env file at root
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

# Get MongoDB connection string from environment
MONGO_URI = os.getenv("MONGO_URI")

# Initialize MongoDB client and database
client = MongoClient(MONGO_URI)
db = client["ecommerce_db"]

# collecetions
users_collection = db["users"]
products_collection = db["products"]
orders_collection = db["orders"]
cart_collection = db["cart"]

