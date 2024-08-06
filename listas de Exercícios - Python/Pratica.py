estoque = ["Maça","Laranja"]

while True:
    op = (input(f"""
======= Estoque =======
        (1) Adicionar Produtos
        (2) Remover Produdos
        (3) Exibir Produtos
        (4) Encerrar Sistema
                
        -"""))
    
    if op == '1':
        prod = input("Digite o Nome do Produto: ")
        estoque.append(prod)

    elif op == '2':
        print(estoque)
        retirar = input("\nDigite o Nome do Item a Ser Removido: ")
        if retirar in estoque:
            estoque.remove(retirar)

    elif op == '3':
        print("\nProdutos em Estoque:",estoque)
    
    elif op == '4':
        print("Tenha um Bom Dia! (^-^)")
        break

    else:
        print("\nOpção Não Listada\n")