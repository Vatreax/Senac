list = []
list_2 = []
for i in range(5):
    list = float(input(f"\nDigite o {i+1}°Número: "))
    print
    list_2.append(list * 5)
print(f"""\nLista de Números Digitados {", ".join(str(i) for i in list_2)}\n""")