# Fábrica do app: monta o Flask, liga as extensões e registra os Blueprints.
# Fica separado em uma função (create_app) para o app ser criado
# só quando precisar, o que evita import circular e facilita testes.
from flask import Flask
from config import Config
from app.extensions import db, migrate, login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app import models  # noqa: F401  (o Migrate precisa enxergar os models)

    from app_postgres.app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app