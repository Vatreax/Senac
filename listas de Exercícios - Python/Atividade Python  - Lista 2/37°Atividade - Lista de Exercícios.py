print("""
Tabela de Comissão e Impostos
+===============================+===================+================+
|       CUSTO DE FÁBRICA        | % DO DISTRIBUIDOR | % DOS IMPOSTOS |
|-------------------------------|-------------------|----------------|
| até R$12.000,00               |         5         |     isento     |
|-------------------------------|-------------------|----------------|
| entre R$12.000,00 e 25.000,00 |        10         |       15       |
|-------------------------------|-------------------|----------------|
| acima de R$25.000,00          |        15         |       20       |
+===============================+===================+================+
      
""")

n1 = float(input("Preço do Carro a ser Adquirido: R$"))

if n1 <= 12000.00:
    dist = n1 * (5/100)
    total = n1 + dist
    print(f"""
          
 Preço Original       = R${n1}
 Taxa do Distribuidor = R${dist}
 Total a ser Pago     = R${total}

""")
    
elif n1 > 12000.00 and n1 <= 25000.00:
    dist = n1 * (10/100)
    imp = n1 * (15/100)
    total = n1 + dist + imp
    print(f"""
          
 Preço Original       = R${n1}
 Taxa do Distribuidor = R${dist}
 Impostos             = R${imp}
 Total a ser Pago     = R${total}

""")
    
elif n1 > 25000.00:
    dist = n1 * (15/100)
    imp = n1 * (20/100)
    total = n1 + dist + imp
    print(f"""
          
 Preço Original       = R${n1}
 Taxa do Distribuidor = R${dist}
 Impostos             = R${imp}
 Total a ser Pago     = R${total}

""")