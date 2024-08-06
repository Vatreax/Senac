n1 = float(input("\nDigite Um Valor Entre 0 e 10: "))

while n1 < 0 or n1 > 10:
    print("Valor Valido")

    if n1 < 0 and n1 > 10:
        print("\nValor Invalido\n")
        n1 = float(input("Digite Um Valor Entre 0 e 10: ")) 
        
    break