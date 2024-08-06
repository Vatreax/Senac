entrada = "S"
saida = "N"

while entrada != saida:
    print("""
    +===============+
    |  Calculadora  |
    +===============+""")
    i= int(input("""Qual a Operação Que Deseja Realizar:
    1 - Soma
    2 - Subtração
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
        re = n1 - n2
        print("\nO Resultado é: ",re)

    elif i == 3:
        n1 = float(input("\nDigite o 1°Número: "))
        n2 = float(input("Digite o 2°Número: "))
        re = n1 / n2
        print("\nO Resultado é: ",re)

    elif i == 4:
        n1 = float(input("\nDigite o 1°Número: "))
        n2 = float(input("Digite o 2°Número: "))
        re = n1*n2
        print("\nO Resultado é: ",re)

    elif i <= 0 or i >= 5:
        print("\nOpção Incorreta")

    entrada = input("""
    Digite:
                    
     S - para continuar
     N - para parar
                    
    """)