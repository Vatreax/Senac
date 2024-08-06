n1 = input("Digite um Número: ")

try:
    n1 = float(n1)
    print(n1)

except ValueError:
    print("\nConversão Falhou!\n")