import json

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

