n1 = int(input("Quantos Metros Quadrados Serão Pintados? "))
gal18 = 80.00
gal3 = 25.00

if n1 <= 6 or n1 <= 21.8:
    print(f"""
          
 Será Necessário 1 Galão de 3.6 Litros
 Preço Total = R${gal3}

""")

elif n1 >= 29.9 or n1 <= 86.4:
    total = gal3 * 4
    print(f"""
          
 Será Necessário 4x um Galão de 3.6 Litros
 Preço Total = R${total}

""")
    
elif n1 >= 86.5 or n1 <= 108:
    
    print(f"""
          
 Será Necessário 1 Galão de 18 Litros
 Preço Total = R${gal18}

""")