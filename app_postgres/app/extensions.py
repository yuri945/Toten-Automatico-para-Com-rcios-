# Cria as extensões (banco, migrate e login) sem ligar a nenhum app ainda.
# Fica separado para os models e as rotas poderem importar o "db"
# sem causar import circular com o __init__.py.
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = "auth.login"