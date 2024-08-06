n1 = float(input("\nPrimeira Nota Do Aluno: "))
n2 = float(input("Segunda Nota Do Aluno: "))

if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10:
    print("\nNotas Invalidas")

else:
    re1 = (n1 + n2) / 2
    print("\nMédia do Aluno: ", re1)