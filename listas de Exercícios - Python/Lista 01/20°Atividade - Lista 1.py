i = 0
quant = int(input("\nQuantos Números Deseja Digitar? "))
list = []

while i < quant:
    i = i + 1
    print("\nDigite um Número entre 0 e 1000")
    n1 = float(input(f"\nDigite o {i}°Número: "))
    if n1 >= 0 and n1 <= 1000:
        list.append(n1)
    else:
        print("Número Invalido")

print("\nMaior Número Digitado:", max(list))
print("Menor Número Digitado:", min(list))
print("\nA Soma de Todos os Valores:", sum(list))