sexo = input("Seu Sexo(Homem/Mulher): ")
altura_baixo_nengue = float(input("Sual Altura: "))

if sexo == "Homem" or sexo == "homem" or sexo == "homi":
    peso = 72.7 * altura_baixo_nengue -58
    print("O seu peso ideal é: ", peso)

elif sexo == "Mulher" or sexo == "mulher":
    peso = 62,1 * altura_baixo_nengue -44,7
    print("O seu peso ideal é: ", peso)

else:
    print("Sexo Invalido")