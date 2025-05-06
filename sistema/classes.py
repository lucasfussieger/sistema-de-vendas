import json

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
    
class vendedor:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def aprovar(self, pedido,):
        pedido.status = 'aprovado'

    def registrar_produto(self, nomeprod, valor, arquivo = 'produtos.json'):
        novo_produto = {'nome': nomeprod, 'valor': valor}

        try:
            with open('produtos'.json, 'r') as file:
                dados = json.load(file)
        
        except FileNotFoundError:

            dados = {'produtos': []}

        dados['produtos'].append(novo_produto)

        with open('produtos'.json, 'w') as file:
            json.dump(dados, file)
            