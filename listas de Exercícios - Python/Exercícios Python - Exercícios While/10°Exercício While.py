entrada = "1"
saida   = "Sair"
cad  = 10
cane = 10
lap  = 10
bor  = 10
reg  = 10

while entrada != saida:

    prod = int(input(f"""
+======================+-------------------
|  Código  |  Produto  |    Quantidade 
+==========+===========|-------------------
|    10    | -Caderno  | {cad}
|    20    | -Caneta   | {cane}
|    30    | -Lápis    | {lap}
|    40    | -Borracha | {bor}
|    50    | -Régua    | {reg}
+======================+-------------------

Digite o Código do Produto que deseja Operar: """))

    while prod == 10:
        print("\n- CADERNO SELECIONADO -")
        açao = input("""
+===============================+
|  Código  |      Operação      |
|----------+--------------------|
|     E    | Entrada do Estoque |
|----------+--------------------|
|     S    |  Saída de Estoque  |
|----------+--------------------|
|     R    |     Relatório      |
|----------+--------------------|
|     X    |       Sair         |
+===============================|

Digite O Código Da Operação: """)
        
        if açao == "E" or açao == "e":
            op = int(input("\nQuantos Cadernos Seram Adicionados: "))
            cad = op + cad
            print("\nAdicionado ao estoque\n")

        elif açao == "S" or açao == "s":
            op = int(input("\nQuantos Cadernos Seram Retirados: "))
            cad = cad - op 
            print("\nRetirado do Estoque\n")

        elif açao == "R" or açao == "r":
            print(f"""
+===========+===-----------------
|  Produto  | Quantidade
|-----------|--------------------
| -Caderno  | {cad}
| -Caneta   | {cane}
| -Lápis    | {lap}
| -Borracha | {bor}
| -Régua    | {reg}
+===========+-------------------
""")
        elif açao == "X" or açao == "x":
            if cad < 0 and cane < 0 and lap < 0 and bor < 0 and reg < 0:
                print("\nQuantidade Invalida em Estoque\n")

            else:
                print(f"""
+===========+===-----------------
|  Produto  | Quantidade
|-----------|--------------------
| -Caderno  | {cad}
| -Caneta   | {cane}
| -Lápis    | {lap}
| -Borracha | {bor}
| -Régua    | {reg}
+===========+-------------------
""")
                prod = 0
        else:
            print("\nCódigo Invalido\n")

        prod = int(input("""
    Deseja Continuar a Operação?
Digite o Código:   10   - Para CONTINUAR
Digite o Número:    0   - Para PARAR
-"""))


    while prod == 20:
        print("\n- CANETA SELECIONADO -")
        açao = input("""
+===============================+
|  Código  |      Operação      |
|----------+--------------------|
|     E    | Entrada do Estoque |
|----------+--------------------|
|     S    |  Saída de Estoque  |
|----------+--------------------|
|     R    |     Relatório      |
|----------+--------------------|
|     X    |       Sair         |
+===============================|

Digite O Código Da Operação: """)
        
        if açao == "E" or açao == "e":
            op = int(input("\nQuantas Canetas Seram Adicionados: "))
            cane = op + cane
            print("\nAdicionado ao estoque\n")

        elif açao == "S" or açao == "s":
            op = int(input("\nQuantas Canetas Seram Retirados: "))
            cane = cane - op 
            print("\nRetirado do Estoque\n")

        elif açao == "R" or açao == "r":
            print(f"""
+===========+===-----------------
|  Produto  | Quantidade
|-----------|--------------------
| -Caderno  | {cad}
| -Caneta   | {cane}
| -Lápis    | {lap}
| -Borracha | {bor}
| -Régua    | {reg}
+===========+-------------------
""")
        elif açao == "X" or açao == "x":
            if cad < 0 and cane < 0 and lap < 0 and bor < 0 and reg < 0:
                print("\nQuantidade Invalida em Estoque\n")

            else:
                print(f"""
+===========+===-----------------
|  Produto  | Quantidade
|-----------|--------------------
| -Caderno  | {cad}
| -Caneta   | {cane}
| -Lápis    | {lap}
| -Borracha | {bor}
| -Régua    | {reg}
+===========+-------------------
""")
                prod = 0
        else:
            print("\nCódigo Invalido\n")

        prod = int(input("""
    Deseja Continuar a Operação?
Digite o Código:   10   - Para CONTINUAR
Digite o Número:    0   - Para PARAR
-"""))

    while prod == 30:
        print("\n- LÁPIS SELECIONADO -")
        açao = input("""
+===============================+
|  Código  |      Operação      |
|----------+--------------------|
|     E    | Entrada do Estoque |
|----------+--------------------|
|     S    |  Saída de Estoque  |
|----------+--------------------|
|     R    |     Relatório      |
|----------+--------------------|
|     X    |       Sair         |
+===============================|

Digite O Código Da Operação: """)
        
        if açao == "E" or açao == "e":
            op = int(input("\nQuantos Lápis Seram Adicionados: "))
            lap = op + lap
            print("\nAdicionado ao estoque\n")

        elif açao == "S" or açao == "s":
            op = int(input("\nQuantos Lápis Seram Retirados: "))
            lap = lap - op 
            print("\nRetirado do Estoque\n")

        elif açao == "R" or açao == "r":
            print(f"""
+===========+===-----------------
|  Produto  | Quantidade
|-----------|--------------------
| -Caderno  | {cad}
| -Caneta   | {cane}
| -Lápis    | {lap}
| -Borracha | {bor}
| -Régua    | {reg}
+===========+-------------------
""")
        elif açao == "X" or açao == "x":
            if cad < 0 and cane < 0 and lap < 0 and bor < 0 and reg < 0:
                print("\nQuantidade Invalida em Estoque\n")

            else:
                print(f"""
+===========+===-----------------
|  Produto  | Quantidade
|-----------|--------------------
| -Caderno  | {cad}
| -Caneta   | {cane}
| -Lápis    | {lap}
| -Borracha | {bor}
| -Régua    | {reg}
+===========+-------------------
""")
                prod = 0
        else:
            print("\nCódigo Invalido\n")

        prod = int(input("""
    Deseja Continuar a Operação?
Digite o Código:   10   - Para CONTINUAR
Digite o Número:    0   - Para PARAR
-"""))

    while prod == 40:
        print("\n- BORRACHA SELECIONADO -")
        açao = input("""
+===============================+
|  Código  |      Operação      |
|----------+--------------------|
|     E    | Entrada do Estoque |
|----------+--------------------|
|     S    |  Saída de Estoque  |
|----------+--------------------|
|     R    |     Relatório      |
|----------+--------------------|
|     X    |       Sair         |
+===============================|

Digite O Código Da Operação: """)
        
        if açao == "E" or açao == "e":
            op = int(input("\nQuantas Borrachas Seram Adicionadas: "))
            bor = op + bor
            print("\nAdicionado ao estoque\n")

        elif açao == "S" or açao == "s":
            op = int(input("\nQuantas Borrachas Seram Retiradas: "))
            bor = bor - op 
            print("\nRetirado do Estoque\n")

        elif açao == "R" or açao == "r":
            print(f"""
+===========+===-----------------
|  Produto  | Quantidade
|-----------|--------------------
| -Caderno  | {cad}
| -Caneta   | {cane}
| -Lápis    | {lap}
| -Borracha | {bor}
| -Régua    | {reg}
+===========+-------------------
""")
        elif açao == "X" or açao == "x":
            if cad < 0 and cane < 0 and lap < 0 and bor < 0 and reg < 0:
                print("\nQuantidade Invalida em Estoque\n")

            else:
                print(f"""
+===========+===-----------------
|  Produto  | Quantidade
|-----------|--------------------
| -Caderno  | {cad}
| -Caneta   | {cane}
| -Lápis    | {lap}
| -Borracha | {bor}
| -Régua    | {reg}
+===========+-------------------
""")
                prod = 0
        else:
            print("\nCódigo Invalido\n")

        prod = int(input("""
    Deseja Continuar a Operação?
Digite o Código:   10   - Para CONTINUAR
Digite o Número:    0   - Para PARAR
-"""))

    while prod == 50:
        print("\n- RÉGUA SELECIONADO -")
        açao = input("""
+===============================+
|  Código  |      Operação      |
|----------+--------------------|
|     E    | Entrada do Estoque |
|----------+--------------------|
|     S    |  Saída de Estoque  |
|----------+--------------------|
|     R    |     Relatório      |
|----------+--------------------|
|     X    |       Sair         |
+===============================|

Digite O Código Da Operação: """)
        
        if açao == "E" or açao == "e":
            op = int(input("\nQuantas Réguas Seram Adicionadas: "))
            reg = op + reg
            print("\nAdicionado ao estoque\n")

        elif açao == "S" or açao == "s":
            op = int(input("\nQuantas Réguas Seram Retiradas: "))
            reg = reg - op 
            print("\nRetirado do Estoque\n")

        elif açao == "R" or açao == "r":
            print(f"""
+===========+===-----------------
|  Produto  | Quantidade
|-----------|--------------------
| -Caderno  | {cad}
| -Caneta   | {cane}
| -Lápis    | {lap}
| -Borracha | {bor}
| -Régua    | {reg}
+===========+-------------------
""")
        elif açao == "X" or açao == "x":
            if cad < 0 and cane < 0 and lap < 0 and bor < 0 and reg < 0:
                print("\nQuantidade Invalida em Estoque\n")

            else:
                print(f"""
+===========+===-----------------
|  Produto  | Quantidade
|-----------|--------------------
| -Caderno  | {cad}
| -Caneta   | {cane}
| -Lápis    | {lap}
| -Borracha | {bor}
| -Régua    | {reg}
+===========+-------------------
""")
                prod = 0
        else:
            print("\nCódigo Invalido\n")

        prod = int(input("""
    Deseja Continuar a Operação?
Digite o Código:   10   - Para CONTINUAR
Digite o Número:    0   - Para PARAR
-"""))

    entrada = input("""
    Deseja Encerrar o Programa?
Aperte QUALQUER Tecla - Para CONTINUAR
Digite  "Sair"         - Para PARAR

- """)

print(f"""+============+-------------------
|  Código  |  Produto  |    Quantidade 
+==========+===========|-------------------
|    10    | -Caderno  | {cad}
|    20    | -Caneta   | {cane}
|    30    | -Lápis    | {lap}
|    40    | -Borracha | {bor}
|    50    | -Régua    | {reg}
+======================+-------------------
""")