n1 = int(input("1°Número Inteiro: "))
n2 = int(input("2°Número Inteiro: "))
n3 = float(input("Número Real: "))

Meta1 = n2/2
re1 = n1 * Meta1

Meta2 = n1 * 3
re2 = Meta2 + n3

re3 = n3 ** 3

print(f"""
O produto do primeiro com a metade do segundo: {re1}

A soma do triplo do primeiro com o terceiro: {re2}
      
O terceiro número digitado ao cubo: {re3}
""")