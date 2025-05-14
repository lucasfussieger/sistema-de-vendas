def show_menu(objeto):
    
    metodos = [m for m in dir(objeto) if callable(getattr(objeto, m)) and not m.startswith("__")]

    print('===funções disponíveis para o usuário===')
    for i, func in enumerate(metodos, start=1):
        print(f"{i}. {func}")

    
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

show_menu(user)