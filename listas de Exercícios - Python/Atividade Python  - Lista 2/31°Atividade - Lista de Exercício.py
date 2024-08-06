n1 = int(input("\nQuantos Kilometros o seu Carro Rodou: "))
n2 = int(input("Quantidade de Gasolina Gasta Nesse Percurso: "))

kilometragem = n1 / n2


if kilometragem < 8:
    print("\nVenda o Seu Carro!")
    print(kilometragem)
    
elif kilometragem >= 8 and kilometragem <= 12:
    print("\nO Seu Carro é Econômico!")
    print(kilometragem)

else:
    print("\nO Seu Carro é Super Econômico!!!")
    print(kilometragem)