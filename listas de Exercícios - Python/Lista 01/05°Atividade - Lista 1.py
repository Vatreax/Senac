city_a = int(input("A População da Cidade A: "))
porcentagem1 = float(input("Porcentagem de Crescimento Populacional da Cidade A: "))
city_b = int(input("A População da Cidade B: "))
porcentagem2 = float(input("Porcentagem de Crescimento Populacional da Cidade B: "))
i = 0

while city_a <= city_b:
    if city_a <= city_b:
        i += 1
        cres1 = city_a * (porcentagem1/100)
        city_a = cres1 + city_a

        cres2 = city_b * (porcentagem2/100)
        city_b = cres2 + city_b

        
    
    if city_a >= city_b:
        print("Dado Incorreto - a População da Cidade A não pode ser maior que a da Cidade B")
        break

    if porcentagem2 >= porcentagem1:
        print("Dado Incorreto - a Porcentagem de Crescimento Populacional da Cidade B não pode ser maior que a da Cidade A")
        break
    



print(f"""
    Anos Necessários Que a População da Cidade A Ultrapasse a Cidade B: {i}
    Crescimento Aproximado Da População da Cidade A: {city_a}
    Crescimento Aproximado Da População da Cidade B: {city_b}

    """)