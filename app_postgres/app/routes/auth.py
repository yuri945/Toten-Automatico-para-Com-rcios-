# Rotas de autenticação (login, cadastro e logout).
# Fica em um Blueprint próprio para separar tudo que é de conta
# das rotas da loja e do admin.
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.extensions import db
from app.models import Usuario
from app.forms.auth import FormCadastro, FormLogin

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/cadastro", methods = ["GET", "POST"])
def criar_conta():

    form_cadastro = FormCadastro()

    if form_cadastro.validate_on_submit():

        usuario = Usuario(username=form_cadastro.username.data,
                            email=form_cadastro.email.data,
                            cpf=form_cadastro.cpf.data)

        usuario.set_senha(form_cadastro.senha.data)

        db.session.add(usuario)
        db.session.commit()

        flash("Conta criada com sucesso!")

        return redirect (url_for("dashboard"))

    return render_template("auth/cadastro.html", form=form_cadastro)