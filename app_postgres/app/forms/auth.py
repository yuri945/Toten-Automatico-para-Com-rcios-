from flask_wtf import FlaskForm
import re
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError # DataRequired = obriga a preencher o campo, EqualTo= ve se senha sao iguais, Length = so permite senha de tal tamanho, ValidationError = mensagem de erro caso tenha erro
from app.models import Usuario


def limpa_cpf(valor):
    return re.sub(r"\D", "", valor) if valor else valor

def limpa_email(valor): # faz com que todo email digitado maisculo ou minusculo seja igual
    return valor.strip().lower() if valor else valor

class FormCadastro(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(),Email()], filters=[limpa_email])
    username = StringField("Nome de usuario", validators=[DataRequired()])
    senha = PasswordField("Senha",validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])
    cpf = StringField("CPF", validators=[DataRequired()], filters=[limpa_cpf])
    botao_confirmacao = SubmitField("Criar Conta")


    def validate_cpf(self, cpf): #valida o cpf em 11 digitos
        if len(cpf.data) != 11:
            raise ValidationError("O CPF deve ter 11 dígitos")
            
        usuario = Usuario.query.filter_by(cpf=cpf.data).first()
        
        if usuario:
            raise ValidationError("CPF já cadastrado")
    
    def validate_email(self, email): # valida o email se já tem no banco de dados 
        usuario = Usuario.query.filter_by(email = email.data).first()
        if usuario:
            raise ValidationError("Email já cadastrado, faça o login para continuar")


    
class FormLogin(FlaskForm):
    email =  StringField("E-mail", validators=[DataRequired(),Email()])
    senha =  PasswordField("Senha",validators=[DataRequired()])
    botao_confirmacao = SubmitField("Entrar")