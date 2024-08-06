n1 = float(input("Nota da 1°Prova: "))
n2 = float(input("Nota da 2°Prova: "))
n3 = float(input("Nota da 3°Prova: "))

media = (n1 + n2 + n3 * 2) / 4

if media >= 60:
    print("Média:", media,"\nAluno foi Aprovado Baixo Nengue, Tá maluco\n")

elif media < 60:
    print("Média", media, "\nAluno foi Reprovado Alto Nengue\n")