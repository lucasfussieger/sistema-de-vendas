import json
import smtplib
from email.message import EmailMessage
from werkzeug import check_password_hash

def confirmacao_email(dest, name_cliente):
    remetente = ''
    senha = ''

    with open('confirmacao.html', 'r') as file:
        html_content = file.read()

    html_content = html_content.replace('{{nome}}', name_cliente)

    msg = EmailMessage()

    msg['subject'] = '=== CADASTRO REALIZADO COM SUCESSO ==='
    msg['from'] = remetente
    msg['to'] = dest
    msg.set_content('olá! seu cadastro foi realizado com sucesso! muito bem vindo ao nosso sistema!')

    msg.add_alternative(html_content, subtype = 'html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(remetente, senha)
            smtp.send_message(msg)
        print('email enviado com sucesso!')

    except Exception as e:
        print(' erro ao enviar:', e)

def show_menu(objeto):
    
    metodos = [m for m in dir(objeto) if callable(getattr(objeto, m)) and not m.startswith("__")]

    print('===funções disponíveis para o usuário===')
    for i, func in enumerate(metodos, start=1):
         return (f"{i}. {func}")

    
    escolha = input("Digite o número da função que deseja executar: ")
    indice = int(escolha)-1
    try:
        if 0 <= indice < len(metodos):
            nome_funcao = metodos[indice]
            funcao = getattr(objeto, nome_funcao)
            return funcao() 
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def to_dict(t): #retorna o objeto formatado em json e salva em um arquivo de acordo com a classe
   
    c = t.__class__.__name__

    try:
        with open(f'{c}.json', 'r') as file:
            dados = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        dados = {}


    if f"{c}" not in dados:
        dados[f"{c}"] = []

    dados[f'{c}'].append(vars(t))
    
    with open(f'{c}.json', 'w') as f:

        json.dump(dados, f, indent=4)
    print('===REGISTRADO NO BANCO DE DADOS===')



def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)