lista = []
imp = 0
par = 0

for i in range(10):
    lista.append(float(input("Digite Um Número:")))

    if i % 2 == 1:
        imp = imp + 1

    if i % 2 == 0:
        par = par + 1

print(f"""

Soma dos Valores: {sum(lista)}

Total de Números Impares : {imp}
Total de Números Pares: {par}
""")