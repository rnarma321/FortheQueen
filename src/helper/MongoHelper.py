from pymongo import MongoClient
from dotenv import load_dotenv
import os
import src.main.Player as Player
import certifi
ca = certifi.where()
load_dotenv()
PASSWORD = os.getenv('PASSWORD')

MONGO = MongoClient("mongodb+srv://roshannarma:"+ PASSWORD + "@forthequeen.v1yel.mongodb.net/FantasyStocks?retryWrites=true&w=majority",tlsCAFile=ca)


def DEFAULTUSER(User):
    return {
        "_id" : User.id,
        "Name": User.name + "#" + User.discriminator,
    }
