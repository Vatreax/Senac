lista = ['a','b','c','d']

try:
    print(lista[0])
    print(lista[1])
    print(lista[2])
    print(lista[3])
    print(lista[4])

except IndexError:
    print("Posição Incorreta")