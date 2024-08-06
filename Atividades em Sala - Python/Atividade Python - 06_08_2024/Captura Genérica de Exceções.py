class Divi():
    while True:
        
        try:
            n1 = float(input("Digite ai, man°1: "))
            n2 = float(input("Digite ai, man°2: "))

            a = n1/n2
            print(a)
            print("\nTenha um Bom Dia! (^-^)")
            break

        except ArithmeticError:
            print("Impossivel Realizar Divisão Por Zero!!!")
            print("Digite um Número ACIMA de Zero\n")

        except ValueError:
            print("Digite um Número!!!")
            print("Digite um Número ACIMA de Zero\n")