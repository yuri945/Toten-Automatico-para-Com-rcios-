from app.extensions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin 

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    senha_hash = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), nullable=True, unique=True)
    is_admin = db.Column(db.Boolean, default=False, nullable=True)

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def checa_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)


@login_manager.user_loader
def load_usuario(id_usuario):
    return db.session.get(Usuario, int(id_usuario))
