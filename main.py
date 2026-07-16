import funcoes
while True:
    print("===================")
    print("     TURBO NET     ")
    print("===================")

    print("1 - Painel Administrador")
    print("2 - Painel Tecnico")
    print("3 - Painel Cliente")
    print("4 - Painel do RH")
    print("5 - Painel do Gerente Financeiro")
    try:
        opcao = int(input("Digite a opção a ser escolhida: "))

    except ValueError:
        print("Opcão Invalida, tente novamente !!!")
        continue
    else:
        match opcao:
            case 1:
                from .funcoes import oi

