lista = []
neg = 0
pos = 0

for i in range(10):
    lista.append(float(input("Digite Um Número:")))

    if i < 0:
        neg =+ 1

    else:
        pos =+ 1

print(f"""

Valores: {len(lista)}

Soma de Números Negativos : {neg}
Soma de Números Positivos : {pos}
""")