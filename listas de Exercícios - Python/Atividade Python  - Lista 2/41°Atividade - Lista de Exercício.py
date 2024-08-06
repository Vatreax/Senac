import math
a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

delt = (b**2) - ((4*a)*c)
print("\nValor de Delta: ", delt)

if a == 0:
    print("Não Há Equação de Segundo Grau.")

elif delt < 0:
    print("Não Existe Raiz.")

elif delt == 0:
    raiz_quadrada = math.sqrt(delt)
    x = (-b + raiz_quadrada) / (2*a)
    print("Exite uma Raiz Unica: ", x)

elif delt > 0:
    raiz_quadrada = math.sqrt(delt)
    x1 = (-b + raiz_quadrada) / (2*a)
    x2 = (-b - raiz_quadrada) / (2*a)
    print("\nRaiz 1:", x1, "\nRaiz 2: ", x2)