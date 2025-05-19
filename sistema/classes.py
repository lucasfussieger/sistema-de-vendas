import json
from datetime import datetime
from funções import to_dict
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'raíssa'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

# Criar banco
with app.app_context():
    db.create_all()

class cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)




    def fazer_pedido(self): 
        return 'fazer pedido'

class vendedor(db.Model):
    __tablename__ = 'vendedores'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha_hash = db.Column(db.String(100), nullable=False)


    def registrar_produto(self, nome, preco):
        novo_produto = produto(nome = nome, preco = preco,vendedor_id = self.id)
        db.session.add(novo_produto)
        db.session.commit()

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)
       

        
class produto(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    preco = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
        
class pedido(db.Model):
    __tablename__ = 'pedidos_pendentes'
    id = db.Column(db.Integer, primary_key=True)
    produto_nome = db.Column(db.String(100), unique=True, nullable=False)
    quantidade = db.Column(db.String(100), nullable=False)
    valor_final = db.Column(db.String(100), nullable=False)
    



            