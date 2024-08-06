print("""
+==================================+
|  Tabuada do Número Selecionado   |
+==================================+
""")

n1 = int(input("Número Selecionado: "))
multi = int(input("Quantas vezes devo multiplicar: "))
contador = 0
multi1 = 0

while contador < multi:
    contador += 1
    r = n1 * contador
    
    print("Tabuada: ", r, "\n")