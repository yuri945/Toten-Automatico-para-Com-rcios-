# Rotas de autenticação (login, cadastro e logout).
# Fica em um Blueprint próprio para separar tudo que é de conta
# das rotas da loja e do admin.
from flask import Blueprint, render_template

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login")
def login():
    return render_template("auth/login.html")