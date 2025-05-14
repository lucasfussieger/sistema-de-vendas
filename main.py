from flask import Flask, render_template, request, redirect, session, url_for
from func import show_menu
#apis todas serão guardadas aqui
app = Flask(__name__)
app.secret_key = 'raíssa'

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['tipo']
        session['tipo'] = usuario

        if usuario == 'cliente':

         return redirect(url_for('painel_cliente'))
        
        return redirect(url_for('painel_vendedor'))
    
    
    return render_template('home.html')


@app.route('/painel_cliente', methods=['GET'])
def painel_cliente():
    usuario = session.get('tipo')

    return render_template('inicio.html', usuario=usuario)

@app.route('/painel_vendedor', methods = ['POST'])
def painel_vendedor():
    usuario = session.get('tipo')
    

if __name__ == "__main__":
    app.run()