entrada = "S"
saida = "N" and "n"
hot = 12.00
sal = 18.50
bacon = 25.50
burg = 17.00
suc = 9.00
refri = 6.00

while entrada != saida:
    print("""
+=================+========+=========+
| Especificação   | Código |  Preço  |
|-----------------|--------|---------|     
| Hot Dog         |  100   |  12.00  |
| X-Salada        |  102   |  18.50  |
| X-BACON         |  103   |  25.50  |
| X-Burguer       |  104   |  17.00  |
| Suco de Laranja |  105   |   9.50  |
| Refrigerante    |  106   |   6.00  |
+=================+========+=========+
      
Selecione um dos códigos para Comprar
""")
    n1 = int(input("Código do Produto: "))
    lista = []
    
    if n1 == 100:
        rounded = (hot)
        print("\nPreço a ser Debitado: R$", rounded)
    
    elif n1 == 102:
        rounded = (sal)
        print("\nPreço a ser Debitado: R$", rounded)

    elif n1 == 103:
        rounded = (bacon)
        print("\nPreço a ser Debitado: R$", rounded)

    elif n1 == 104:
        rounded = (burg)
        print("\nPreço a ser Debitado: R$", rounded)

    elif n1 == 105:
        rounded = (suc)
        print("\nPreço a ser Debitado: R$", rounded)

    elif n1 == 106:
        round = (refri)
        print("\nPreço a ser Debitado: R$", rounded)
    
    entrada = input("""
    Deseja Continuar Comprando:
                   
    S - Para Continuar
    N - Para Sair
                    
-""")
