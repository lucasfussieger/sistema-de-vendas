import json
from datetime import datetime

class cliente:

    def __init__(self,nome,senha,email):
        self.nome = nome
        self.senha = senha
        self.email = email
        
        
class produto:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def to_dict(self, nome, valor):
        return {
    
        }
        

class pedido:
    def __init__(self,cliente, produto, quantprod, valor, status = 'pendente'):
        self.cliente = cliente
        self.produto = produto
        self.quantprod = quantprod
        self.valor = valor
        self.status = status
        self.data_pedido = datetime.now().isoformat()

    
class vendedor:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def registrar_produto(self, arquivo = 'produtos.json'):
        nomeprod = str(input('digite o nome do produto: '))
        valor = int(input('digite o valorunitário do produto'))
        novo_produto = {'nome': nomeprod, 'valor': valor}

        dados = {'produtos': []}

        dados['produtos'].append(novo_produto)

        with open('produtos.json', 'w') as file:
            json.dump(dados, file, indent=4)

        print('=== PRODUTO REGISTRADO COM SUCESSO===')
            