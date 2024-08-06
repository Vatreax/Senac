entrada = "S"
saida = "N" and "n"

while entrada != saida:
    print("""
    +===============+
    |  Calculadora  |
    +===============+
    """)
    i= int(input("""Qual a Operação Que Deseja Realizar:
                 
    1 - Soma
    2 - Maior pelo Menor
    3 - Divisão
    4 - Multiplicação      
                       
    - """))


    if i == 1:
        n1 = float(input("\nDigite o 1°Número: "))
        n2 = float(input("Digite o 2°Número: "))
        re = n1 + n2
        print("\nO Resultado é: ", re)

    elif i == 2:
        n1 = float(input("\nDigite o 1°Número: "))
        n2 = float(input("Digite o 2°Número: "))
        re = max(n1,n2)
        re1 = min(n1,n2)
        re2 = re - re1
        print("\nO Maior Número é: ", re, "\nPela Diferença de: ", re2)

    elif i == 3:
        n1 = float(input("\nDigite o 1°Número: "))
        n2 = float(input("Digite o 2°Número: "))
        if n1 == 0 or n2 == 0:
            print("Valor Invalido - Não Utilizar 0")
        else:
            re = n1/n2
            print("\nO Resultado é: ", re)

    elif i == 4:
        n1 = float(input("\nDigite o 1°Número: "))
        n2 = float(input("Digite o 2°Número: "))
        if n1 == 0 or n2 == 0:
            print("Valor Invalido - Não Utilizar 0")
        else:
            re = n1*n2
            print("\nO Resultado é: ", re)

    elif i <= 0 or i >= 5:
        print("\nOpção Incorreta")

    entrada = input("""
    Digite:
                    
     S - para continuar
     N - para parar
                    
    """)