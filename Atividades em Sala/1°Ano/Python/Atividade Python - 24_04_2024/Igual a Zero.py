i = 0
total = 0
while i < 10:
    i += 1
    f = float(input("Insira o Número: "))
    total = f + total
    if f == 0:
        break
print("O resultado foi: ", total)