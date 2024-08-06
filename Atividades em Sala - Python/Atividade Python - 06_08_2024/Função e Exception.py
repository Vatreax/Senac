class Impedir(Exception):
    n = "ola"
    if(n=="ola"):
        print("nao :(")

def tratamento(n):
    try:
        n = float(n)
    except ArithmeticError:
        print("Impossivel Realizar Divisão Por Zero!!!")
    except ValueError:
        print("Digite um Número Válido")
    except Impedir:
        print("Poxa")

v = input("Digite ai°1: ")
tratamento(v)