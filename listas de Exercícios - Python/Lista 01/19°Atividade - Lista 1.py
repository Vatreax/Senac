i = 0
quant = int(input("Quantos Números Deseja Digitar? "))
list = []

while i < quant:
    i = i + 1
    n1 = float(input(f"\nDigite o {i}°Número: "))
    list.append(n1)

print("\nMaior Número Digitado:", max(list))
print("Menor Número Digitado:", min(list))
print("\nA Soma de Todos os Valores:", sum(list))