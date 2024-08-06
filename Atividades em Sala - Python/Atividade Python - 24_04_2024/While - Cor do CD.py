cd_azul = 20.00
cd_laranja = 30.00
cd_roxo = 40.00
cd_marrom = 50.00

entrada = "S"
saida = "N" and "n"

total = 0

while entrada != saida:

    print("""
    ============================================
    ||||||||||||| Loja CDs Sistems |||||||||||||
    ============================================
         
    Opções de CD:

    1 - Azul = R$20,00
    2 - Laranja = R$30,00
    3 - Roxo = R$40,00
    4 - Marrom = R$50,00
         
   """)

 
    i = int(input("Qual CD de sua escolha: "))

    if i <= 0 or i>=5: 
        print("\nCD invalido\n")

    if i == 1:
        print("R$", cd_azul)
        cd_escolhido = cd_azul

    if i == 2:
        print("R$", cd_laranja)
        cd_escolhido = cd_laranja
    if i == 3:
        print("R$", cd_roxo)
        cd_escolhido = cd_roxo
    if i == 4:
        print("R$", cd_marrom)    
        cd_escolhido = cd_marrom
    i += 1

    total = total + cd_escolhido

    entrada = input("Deseja Continuar (digite: S/N)? ")
    print("Valor final: R$", total)
