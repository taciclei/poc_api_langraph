import os
from dotenv import load_dotenv

load_dotenv()  # Charger les variables d'environnement depuis .env

class Config:
    APP_ENV = os.getenv("APP_ENV")
    APP_PORT = os.getenv("APP_PORT")
    APP_HOST = os.getenv("APP_HOST")
    LANGGRAPH_CONFIG_PATH = os.getenv("LANGGRAPH_CONFIG_PATH")
