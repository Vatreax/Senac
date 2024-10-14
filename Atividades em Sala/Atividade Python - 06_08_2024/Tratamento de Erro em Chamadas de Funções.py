def tratamento(n):
    try:
        n = float(n)
        print(n)
    except ValueError:
        print("Digite um Número Válido")

v = input("Digite ai: ")
tratamento(v)