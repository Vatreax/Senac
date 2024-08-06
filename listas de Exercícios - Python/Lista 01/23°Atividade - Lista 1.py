n1 = int(input("Verificar Números Primos até: "))
mult=0

for i in range(2,n1):
    if (n1% i == 0):
        print("Múltiplo de", i)
        mult += 1

if(mult == 0):
    print("É primo")
else:
    print(f"Tem {mult} múltiplos acima de 2 e abaixo de {n1}")