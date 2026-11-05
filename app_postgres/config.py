# Configurações do app (chave secreta e banco), lidas do arquivo .env.
# Fica separado para não deixar senha dentro do código
# e poder trocar de banco sem mexer no resto.
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False