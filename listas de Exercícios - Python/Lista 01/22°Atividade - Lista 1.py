n = int(input("Verificar numeros primos ate: "))
mult=0

for i in range(2,n):
    if (n % i == 0):
        mult += 1

if(mult == 0):
    print("É primo")
else:
    print("Não é Primo")