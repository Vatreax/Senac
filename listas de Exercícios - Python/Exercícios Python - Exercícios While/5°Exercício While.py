entrada = "S"
parar = "N" and "n"

while entrada != parar:
    city_a = int(input("A População da Cidade A: "))
    city_b = int(input("A População da Cidade B: "))
    porcentagem1 = float(input("Porcentagem de Crescimento Populacional"))
    print("%")
    porcentagem2 = 
    i = 0

    while city_a <= city_b:
    
        cres1 = (city_a * 3)/100
        city_a = cres1 + city_a

        cres2 = (city_b * 1.5)/100
        city_b = cres2 + city_b

        i += 1

    
    print(f"""
    Anos Necessários Que a População da Cidade A Ultrapasse a Cidade B: {i}
    Crescimento Aproximado Da População da Cidade A: {city_a}
    Crescimento Aproximado Da População da Cidade B: {city_b}

    """)

    entrada = input("""
                    
Digite:
  S - para Continuar
  N - para Parar
""")