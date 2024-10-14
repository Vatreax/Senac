print("""
-------------------------------
     20 Valores Inteiros
-------------------------------
""")

n1 = int(input("\n 1° Número: "))
n_int = []
i = 1
contador = 2
soma = 0

if n1 < 0:
    n_int.append(n1)

while contador <= 20:
    contador += 1
    i += 1
    n1 = int(input(f"\n {i}° Número: "))

    if n1 > 0:
        soma = n1 + soma

    if n1 < 0:
        n_int.append(n1)
    
    
print("\n\nSoma de Números Positivos: ", soma)
print("\nQuantidade dos Números Negativos: ", n_int,"\n")