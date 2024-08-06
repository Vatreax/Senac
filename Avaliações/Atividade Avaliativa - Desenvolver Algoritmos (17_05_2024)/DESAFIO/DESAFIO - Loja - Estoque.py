prod = ["Sorvete - Alimento: Frio - Código 1","Escova de Dente - Higiene: Bocal - Código 2", "Frigideira - Item: Cozinha - Código 3","Tesoura - Item: Escritório - Código 4 "]
quanti = [10,12,5,6]
preço = [10.00,6.25,39.99,4.15]

matricula = input("""\nVocê é um funcionario da loja?
Digite a Matricula de 6 Digitos - FUNCIONÁRIO
Digite QUALQUER tecla           - CLIENTE
- """)

while len(matricula) < 6 or len(matricula) > 6:
    print("\nSeja Bem-Vindo a Loja Senac Hub\n")
    nome = input("Seu Nome: ")
    cpf = input("""Seu CPF: """)

    while len(cpf) < 11 or len(cpf) > 11:
        cpf = input("""
            ERRO - CPF INVALIDO
Digite Novamente o seu CPF ou "DIGITE 0" para ENCERRAR o Sistema
    - """)
        if cpf == "0":
            break

    if cpf == "0":
        break

    print("\n----- |LISTA DE PRODUTOS| -----")
    for i in prod:
        print(i)
    n = 0
    print("")
    for a in preço:
        n+=1
        print(f"Preço do Produto {n}: R$", a)

    carrinho = 0
    ent = "1"
    saida = "N"

    while ent != saida:
        sele = int(input("\nDigite o Código do Produto Desejado: "))

        print(prod[sele-1],"\nPreço: R$",preço[sele-1])
        
        carrinho = carrinho + preço[sele-1]
        print("Seu Carrinho: R$", carrinho)

        ent = input("""
Digite Qualquer Tecla - Para CONTINUAR a Compra
Digite [ 0 ]          - para PARAR

- """)
        if ent == "0":
            print("\n----------- |COMPRA ENCERRADA| ----------- \n")
            break
    imp_nacional = carrinho * (7/100)
    imp_estadual = carrinho * (8/100)
    imp_municipal = carrinho * (12/100)
    preço_total = carrinho + imp_estadual + imp_nacional + imp_municipal 

    i = 0
    while i == 0:
        print("Valor Total: R$", round(preço_total,2))
        pag = input("""\nSelecione um Método de Pagamento: 

        |1|Pix 
        |2|Cartão de Débito
        |3|Cartão de Crédito
        |4|Dinheiro
        |5|Cancelar Compra

        - """)
    
        while pag == "1":
            print("\n--- Pix Selecionado ---\n")
            saldo = float(input("Digite o Seu Saldo: R$"))
            
            if saldo < preço_total:
                print("""
+------------------------------------+
|        SALDO INSUFICIENTE          |
|Selecione outro Método de Pagamento |
+------------------------------------+
""")
                break

            elif saldo >= preço_total:
                re = saldo - round(preço_total,2)
                print(f"""\nCompra Realizada com Sucesso - Obrigado por Comprar na Senac Hub\nTenha um Ótimo Dia, {nome} <3 \nO seu Saldo atual: R${round(re,2)}

            NOTA FISCAl
    Suas Compras      - R${round(carrinho,2)}
    Imposto Nacional  - R${round(imp_nacional,2)}
    Imposto Estadual  - R${round(imp_estadual,2)}
    Imposto Municipal - R${round(imp_municipal,2)}
    Preço Total       - R${round(preço_total,2)}
    """)                
            i+=1
            break
        while pag == "2":
            print("\n--- Débito Selecionado ---\n")
            saldo = float(input("Digite o Seu Saldo: R$"))
            
            if saldo < preço_total:
                print("""
+------------------------------------+
|        SALDO INSUFICIENTE          |
|Selecione outro Método de Pagamento |
+------------------------------------+
""")
                break

            elif saldo >= preço_total:
                re = saldo - round(preço_total,2)
                print(f"""\nCompra Realizada com Sucesso - Obrigado por Comprar na Senac Hub\nTenha um Ótimo Dia, {nome} <3 \nO seu Saldo atual: R${round(re,2)}

            NOTA FISCAl
    Suas Compras      - R${round(carrinho,2)}
    Imposto Nacional  - R${round(imp_nacional,2)}
    Imposto Estadual  - R${round(imp_estadual,2)}
    Imposto Municipal - R${round(imp_municipal,2)}
    Preço Total       - R${round(preço_total,2)}
    """)                
            i+=1
            break

        while pag == "3":
            print("\n--- Crédito Selecionado ---\n")
            saldo = float(input("Digite o Seu Saldo: R$"))
            
            if saldo < preço_total:
                print("""
+------------------------------------+
|        SALDO INSUFICIENTE          |
|Selecione outro Método de Pagamento |
+------------------------------------+
""")
                break
            

            elif saldo >= preço_total:
                re = saldo - round(preço_total,2)
                print(f"""\nCompra Realizada com Sucesso - Obrigado por Comprar na Senac Hub\nTenha um Ótimo Dia, {nome} <3 \nO seu Saldo atual: R${round(re,2)}

            NOTA FISCAl
    Suas Compras      - R${round(carrinho,2)}
    Imposto Nacional  - R${round(imp_nacional,2)}
    Imposto Estadual  - R${round(imp_estadual,2)}
    Imposto Municipal - R${round(imp_municipal,2)}
    Preço Total       - R${round(preço_total,2)}
    """)            
            i+=1   
            break

        while pag == "4":
            print("\n--- Dinheiro Selecionado ---\n")
            saldo = float(input("Quanto será Entregue: R$"))
            
            if saldo < preço_total:
                print("""
+------------------------------------+
|        VALOR INSUFICIENTE          |
|Selecione outro Método de Pagamento |
+------------------------------------+
""")
                break
            
            elif saldo == preço_total:
                re = saldo - round(preço_total,2)
                print(f"""\nCompra Realizada com Sucesso - Obrigado por Comprar na Senac Hub\nTenha um Ótimo Dia, {nome} <3

            NOTA FISCAl
    Suas Compras      - R${round(carrinho,2)}
    Imposto Nacional  - R${round(imp_nacional,2)}
    Imposto Estadual  - R${round(imp_estadual,2)}
    Imposto Municipal - R${round(imp_municipal,2)}
    Preço Total       - R${round(preço_total,2)}
    """)            
                i+=1    
                break

            elif saldo > preço_total:
                re = saldo - round(preço_total,2)
                print(f"""\nCompra Realizada com Sucesso - Obrigado por Comprar na Senac Hub\nTenha um Ótimo Dia, {nome} <3 \nO seu Troco: R${round(re,2)}

            NOTA FISCAl
    Suas Compras      - R${round(carrinho,2)}
    Imposto Nacional  - R${round(imp_nacional,2)}
    Imposto Estadual  - R${round(imp_estadual,2)}
    Imposto Municipal - R${round(imp_municipal,2)}
    Preço Total       - R${round(preço_total,2)}
    """)            
            i+=1    
            break

        while pag == "5":
            i+=1
            break
    print("\nTenha um Bom Dia!")
    break


while len(matricula) == 6:
    print("""
-------- FUNCIONÁRIO REGISTRADO --------
          Bem-Vindo ao Estoque
""")

    nome = input("Seu Nome: ")
    data_nasc = (input("Data de Nascimento: "))
    cpf = (input("Seu CPF: "))

    while len(cpf) < 11 or len(cpf) > 11:
        cpf = input("""
            ERRO - CPF INVALIDO
Digite Novamente o seu CPF ou "DIGITE 0" para ENCERRAR o Sistema
    - """)
        if cpf == "0":
            break

    if cpf == "0":
        break
    
    i = 0
    while i == 0:
        açao = input("""
+===============================+
|  Código  |      Operação      |
|----------+--------------------|
|     E    | Atualizar Estoque  |
|----------+--------------------|
|     S    | Adicionar Produtos |
|----------+--------------------|
|     R    | Consultar Estoque  |
|----------+--------------------|
|     X    |       Sair         |
+===============================|

Digite O Código Da Operação: """)

        while açao == "E" or açao == "e":
            print("\n--- Operação Selecionada - Atualizar Estoque ---\n")
            for a in prod:
                print(a)
            print("")
            n = 0
            for c in preço:
                n += 1
                print(f"Preço do Produto {n}: ", c)
            print("")
            n = 0
            for b in quanti:
                n+=1
                print(f"Quantidade do Produto {n}: ", b)


            sele = int(input("\nDigite o Código do Produto Desejado: "))
            print(prod[sele-1],"\nQuantidade do Produto:", quanti[sele-1])
            ope = input("""Digite o Código das Operações Abaixo:
                        
        |1|Entrada de Estoque
        |2|Saida de Estoque
        |3|Alterar Preço
        |4|Cancelar Operação
-""")
            if ope == "1":
                calculo = int(input("\nQuantos Produtos Serão Adicionados: "))
                quanti[sele-1] = quanti[sele-1] + calculo
                for a in prod:
                    print(a)
                print("")
                n = 0
                for c in preço:
                    n += 1
                    print(f"Preço do Produto {n}: ", c)
                print("")
                n = 0
                for b in quanti:
                    n+=1
                    print(f"Quantidade do Produto {n}: ", b)
                
                print("""
+----------------------------------+
|  Operação Realizada Com Sucesso  |
+----------------------------------+
""")

                break

            elif ope == "2":
                calculo = int(input("\nQuantos Produtos Serão Retirados: "))
                if calculo > quanti[sele-1]:
                    print("""
+------------------------------------------------+
|               OPERAÇÃO CANCELADA               |
|Não Há Quantidade o Suficiente Para Ser Retirado|
+------------------------------------------------+
""")
                    break

                elif calculo < quanti[sele-1]:
                    quanti[sele-1] = quanti[sele-1] - calculo
                    for a in prod:
                        print(a)
                    print("")
                    n = 0
                    for c in preço:
                        n += 1
                        print(f"Preço do Produto {n}: ", c)
                    print("")
                    n = 0
                    for b in quanti:
                        n+=1
                        print(f"Quantidade do Produto {n}: ", b)

                    print("""
+----------------------------------+
|  Operação Realizada Com Sucesso  |
+----------------------------------+
""")
                    break

                elif calculo == quanti[sele-1]:
                    quanti[sele-1] = quanti[sele-1] - calculo
                    print("""
+-----------------------------------------------------------+
|  AVISO - A Quantidade do Produto Selecionado Esta Zerado  |
+-----------------------------------------------------------+
""")
                    for a in prod:
                        print(a)
                    print("")
                    n = 0
                    for c in preço:
                        n +=1
                        print(f"Preço do Produto {n}: ", c)
                    print("")
                    n = 0
                    for b in quanti:
                        n+=1
                        print(f"Quantidade do Produto {n}: ", b)

            elif ope == "3":
                n1 = float(input("Digite o novo Valor: "))
                preço[sele-1] = n1
                n = 0
                print("""
+----------------------------------+
|  Operação Realizada Com Sucesso  |
+----------------------------------+
""")
                break
                
            elif ope == "4":
                break
        while açao == "S" or açao == "s":
            print("\n--- Operação Selecionada - Adicionar Produtos ---\n")
            for a in prod:
                print(a)
                print("")
            n = 0
            for b in quanti:
                n += 1
                print(f"Quantidade do Produto {n}: ", b)

            adicionar = input("""
Adicione o Produto Seguindo a Ordem da Lista e o Exemplo Abaixo:
'Nome do Produto - Tipo: Subtipo - Código x'

- """)
            quantidade = int(input("A Quantidade do Produto Adicionado: "))
            preço_ad = float(input("Digite o Valor Da Unidade Do Produto"))

            prod.append(adicionar)
            quanti.append(quantidade)
            preço.append(preço_ad)

            for a in prod:
                print(a)
            print("")
            n = 0
            for c in preço:
                n += 1
                print(f"Preço do Produto {n}: ", c)
            print("")
            n = 0
            for b in quanti:
                n += 1
                print(f"Quantidade do Produto {n}: ", b)
            print("\n--- Operação Realizada Com Sucesso ---\n")
            break
        while açao == "R" or açao == "r":
            for a in prod:
                print(a)
            print("")
            n = 0
            for c in preço:
                n += 1
                print(f"Preço do Produto {n}: ", c)
            print("")
            n = 0
            for b in quanti:
                n+=1
                print(f"Quantidade do Produto {n}: ", b)
            break

        if açao == "X" or açao == "x":
            print(f"\nTenha Um Bom Dia, {nome} <3\n")
            break
    if açao == "X" or açao == "x":
        break