user = (input("Digite o Nome de Usuário: "))
sen = (input("Digite a Senha: "))

while user == sen:
    print("Erro - Favor, Não Digitar um Nome IGUAL a Senha.")
    user = (input("\nDigite o Nome de Usuário: "))
    sen = (input("Digite a Senha: "))

    