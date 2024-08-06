city_a = 80000
city_b = 200000
i = 0

while city_a <= city_b:
    
    cres1 = (city_a * 3)/100
    city_a = cres1 + city_a

    cres2 = (city_b * 1.5)/100
    city_b = cres2 + city_b

    i += 1

    
print(f"""
Anos Necessários Para se Ultrapassar a População: {i}
Crescimento Aproximado Da População da Cidade A: {city_a}
Crescimento Aproximado Da População da Cidade B: {city_b}

""")