while True:
    print("Resolva as Questões e Ganhe Pontos!")
    i=0

    quest1 = input("Quem proclamou a independência do Brasil? ")

    if quest1 == "Dom Pedro I":
        print("\nCerta Resposta!\n")
        i=+1

    elif quest1 != "Dom Pedro I":
        print("\nResposta Errada!\n")

    quest2 = input("Quem fez o papel de Han Solo e Indiana Jones? ")

    if quest2 == "Harrison Ford":
        print("\nResposta Certa!\n")
        i+=1
    
    elif quest2 != "Harrison Ford":
        print("\nResposta Errada\n")

    quest3 = input("A capita dos EUA é a Washington D.C\nsim ou não? ")
    if quest3 == "sim":
        print("\nCerta Resposta!\n")
        i+=1
    elif quest3 != "sim":
        print("\nReposta Errada!\n")

    if i == 3:
        print("Parábens Você Ganhou... Nada!")
        break

    elif i < 3:
        print("Qualé, não acertou essas fáceis")
        break