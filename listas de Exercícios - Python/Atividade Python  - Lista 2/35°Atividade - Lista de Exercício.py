n1 = float(input("preço do produto: R$"))

if n1 > 100000.00:
    com = n1 * (16/100)
    total = n1 + 700 + com  
    print("Total de Comissão a ser Paga: R$", total)

elif n1 < 100000.00 and n1 >= 80000.00:
    com = n1 * (14/100)
    total = n1 + 650 + com  
    print("Total de Comissão a ser Paga: R$", total)

elif n1 < 80000.00 and n1 >= 60000.00:
    com = n1 * (14/100)
    total = n1 + 600 + com  
    print("Total de Comissão a ser Paga: R$", total)

elif n1 > 60000.00 and n1 >= 40000.00:
    com = n1 * (14/100)
    total = n1 + 550 + com  
    print("Total de Comissão a ser Paga: R$", total)

elif n1 > 40000.00 and n1 >= 20000.00:
    com = n1 * (14/100)
    total = n1 + 500 + com  
    print("Total de Comissão a ser Paga: R$", total)

elif n1 < 20000.00:
    com = n1 * (14/100)
    total = n1 + 400 + com  
    print("Total de Comissão a ser Paga: R$", total)