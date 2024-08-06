lista = []
i = 0
while i < 5:
    i += 1
    n1 =(float(input(f"\nDigite o {i}°Número: ")))
    lista.append(n1)
print("\nA Soma dos Números Digitados:", sum(lista),"\n")
re = sum(lista)/5
print("A Média dos Números Digitados:", re)