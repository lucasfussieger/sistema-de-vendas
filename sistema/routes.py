from flask import Flask, render_template, request, redirect, session, url_for, flash
from funções import show_menu
from classes import cliente,produto,pedido, app, db
from flask_sqlalchemy import SQLAlchemy




#apis todas serão guardadas aqui

# Criar banco
with app.app_context():
    db.create_all()


@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
      usuario = request.form['tipo']
      session['usuario'] = usuario
         
      return redirect(url_for('login'))

    return render_template('home.html')

@app.route('/login', methods = ['GET','POST'])
def login():
   if request.method == 'POST':
      if request.form['modo'] == 'cadastrar':

        return redirect(url_for('cadastrar',))
      
      return redirect(url_for('entrar'))
   return render_template('login.html')

@app.route('/cadastrar', methods = ['GET','POST'])
def cadastrar():
   if request.method == 'POST':   
      user = session['usuario']

      if user == 'vendedor':
         return 'vendedor n pode se cadastrar, apenas entrar'
      else:
         nome = str(request.form['nome'])
         email = request.form['email']
         senha = request.form['senha']
         senha_confirmacao = request.form['senha_confirmacao']
         if senha == senha_confirmacao:
            novo_cliente = cliente(nome=nome,email=email, senha=senha)
            db.session.add(novo_cliente)
            db.session.commit()

            return redirect(url_for('store'))
         flash(' senhas não batem')
         return render_template('cadastro.html')

   return render_template('cadastro.html')

@app.route('/store', methods = ['GET', 'POST'])
#aqui o html renderizado irá mostrar um abaixo do outro os produtos registrados
# o produto mostrado será um botão com informação de nome e valor do produto
#a quantidade de produtos mostrados dependerá de quantos produtos há na lista de pedidos
# ao clicar no botão o usuario é levado para um html que mostra mais informações do cliente, 
# ali ele pode digitar quanto quer daquele produto, e clicar em fazer pedido, que cria um pedido com as informações selecionadas

def store():
   produtos = produto.query.all()
   return render_template('store.html', produtos=produtos)

@app.route('/entrar', methods = ['GET', 'POST'])
# aqui mostra um html que pede email e senha, checa se esta no db,se sim carrega /store,
#  senão, recarregua com um flash dizendo q não consta no db
def entrar():
   return render_template


@app.route('/fazer_pedido', methods = ['GET', 'POST'])
#aqui gera um html com as inforamçoes do produto selecionado em /store
#tem um input para a quantidade do produto
#botão fazer pedido em baixo
#cria o pedido com o nome do cliente que fez e envia ao banco de dados
#retorna um html com 'pedido feito'

def fazer_pedido():
   return

@app.route('/registrar_produto', methods = ['GET','POST'])
def registrar_produto():
   if 'usuario' not in session:
        return redirect(url_for('login'))

   if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        descricao = request.form['descricao']

        produto_c = produto(nome=nome, preco=preco, descricao=descricao)
        db.session.add(produto_c)
        db.session.commit()

        return f'Produto "{nome}" registrado com sucesso! <a href="{url_for("dashboard")}">Voltar ao dashboard</a>'

   return render_template('registrar_produto.html')

@app.route('/entrar', methods = ['GET', 'POST'])
def entrar():

   if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        


        user = session['usuario'].query.filter_by(email=email).first()

        if user and user.verificar_senha(senha):
            return redirect(url_for('dashboard'))
        else:
            return 'Vendedor não existe ou senha inválida', 401

   return render_template('entrar.html')

if __name__ == "__main__":
    app.run()

