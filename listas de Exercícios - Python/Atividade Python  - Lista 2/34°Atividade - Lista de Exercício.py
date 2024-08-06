print("""
+== TABELA DE PREÇOS ==+=======================+
|    Preço Antigo      | Percentual de Aumento |
| até R$ 50            |          5%           |
|----------------------|-----------------------|
| entre R$ 50 e R$ 100 |         10%           | 
|----------------------|-----------------------|
| acima de R$ 100      |         15%           |
+======================+=======================+
""")
n1 = float(input("Preço do Produto: R$"))

if n1 <= 50:
    perca = n1 * (5/100)
    total = n1 + perca
    print("Correção do Preço: R$", total)

elif n1 > 50 or n1 <= 100:
    perca = n1 * (10/100)
    total = n1 + perca
    print("Correção do Preço: R$", total)

elif n1 > 100:
    perca = n1 * (15/100)
    total = n1 + perca
    print("Correção do Preço: R$", total)