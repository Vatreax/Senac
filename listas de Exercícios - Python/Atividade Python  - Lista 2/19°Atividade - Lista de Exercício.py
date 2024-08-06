n1 = input("\nDigite um Número: ")
soma = 0
i = 0

if int(n1) <= 0:
    print("Número Invalido")

else:
    while i < len(n1):
        soma += int(n1[i])
        i += 1

print("\nA soma dos Número é: ", soma)
