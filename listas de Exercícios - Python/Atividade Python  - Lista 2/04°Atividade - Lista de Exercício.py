n1 = float(input("1°Número: "))
n2 = float(input("2°Número: "))
n3 = float(input("3°Número: "))

if n1 < n2 and n2 < n3:
    print("\nOs Seguintes Números Estão em Ordem Crescente: ", n1, " - ", n2, " - ", n3, ".")
elif n1 > n2 and n2 > n3:
    print("\nOs Seguintes Números Estão em Ordem Decrescente: ", n1, " - ", n2, " - ", n3, ".")
else:
    print("\nNão há ordem.")