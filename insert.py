import pymongo

from utils.database import get_mongo_client
from utils.config import Config

consulta = {
        "fecha": "hoy",
        "paciente" : "yo"
    }

config = Config()

client = get_mongo_client(config)
database = client.nutridb
collection = database.consultas
collection.insert_one(consulta)