import classes

print('bem vindo ao sistema de compras 3000 n\ vamos iniciar seu cadastro!')
cadastro = int(input('deseja logar como cliente(1) ou vendedor(2)?: '))
nome = input('digite seu nome: ')
email = input('digite seu email: ')
senha = input('digite sua senha: ')

if cadastro == 1:
    user = classes.cliente(nome,senha,email)

    c = input(str('deseja realizar uma compra?s/n'))
    classes.cliente.compra
elif cadastro == 2:
    user = classes.vendedor(nome,email,senha)
    print('vendedor cadastrado')
nomeprodu= input('nome do produto')
valor = input('valor do produto')
user.registrar_produto(nomeprodu, valor)

