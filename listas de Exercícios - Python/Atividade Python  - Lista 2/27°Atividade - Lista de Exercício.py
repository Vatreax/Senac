n1 = float(input("\nValor de A: "))
n2 = float(input("Valor de B: "))
n3 = float(input("Valor de C: "))

lado1 = n1 + n2
lado2 = n2 + n3
lado3 = n3 + n1

if lado1 + lado2 > lado3 and lado3 + lado1 > lado2 and lado2 + lado3> lado1:
    print("\nOs Valores são os de um Triângulo")

    if n1 == n2 and n2 == n3 and n3 == n1:
        print("\nOs lados do Triângulo Correspondem a um Triângulo Equilátero.\n")

    elif n1 == n2 or n1 == n3 or n2 == n1 or n2 == n3 or n3 == n1 or n3 == n2:
        print("\nOs lados do Triângulo Correspondem a um Triângulo Isósceles.\n")

    elif n2 != n3 != n1:
        print("\nOs lados do Triângulo Correspondem a um Triângulo Escaleno.\n")
        
else:
    print("Os Valores não são os de um Triângulo")