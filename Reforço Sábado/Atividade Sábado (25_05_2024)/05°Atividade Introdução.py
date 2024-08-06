list_par = []
list_impar = []
i_impar = 0

for i in range(11):
    print(i)

    if i % 2 == 0:
        list_par.append(i)

    else:
        list_impar.append(i)

print(f"""
Quantidade de Números Pares: {len(list_par)}
Números Pares: {list_par}
Soma dos Números Pares: {sum(list_par)}""")

print(f"""
Quantidade de Números Impares: {len(list_impar)}
Números Impares: {list_impar}""")