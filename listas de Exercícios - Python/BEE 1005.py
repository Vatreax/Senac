listas = []

while True:

    op = input(f"""
    Selecione a Operação:
    adicionar 
    sair
    
    - """)

    if op == "adicionar":
        nome = (input("Digite o Nome do Cliente: "))
        rg = (input("Digite o RG do Cliente: "))
        cpf = input("Digite o CPF do CLiente: ")
        telefone = input("Digite o Telefone do Cliente: ")
        listas.append([nome, rg, cpf, telefone])

    elif op == "sair":
        for lista in listas:
            print(f"""
====================
Nome: {lista[0]}, RG: {lista[1]}, CPF: {lista[2]}, Telefone: {lista[3]}
""")
        break
    else:
        print("\nOpção Não Listada\n")