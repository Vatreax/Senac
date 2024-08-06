Alunos = [
    ('Genivaldo',10),
    ('Gislaine',6),
    ('Genilda',8)
]
print(Alunos)

Aluno1 = Alunos[0]
Aluno1_1 = Aluno1[0]
Nota1 = Aluno1[1]
print("\n",Aluno1_1,Nota1)

Aluno2 = Alunos[1]
Aluno2_2 = Aluno2[0]
Nota2 = Aluno2[1]
print("\n",Aluno2_2,Nota2)

Aluno3 = Alunos[2]
Aluno3_3 = Aluno3[0]
Nota3 = Aluno3[1]
print("\n",Aluno3_3,Nota3)

med = (Nota1 + Nota2 + Nota3) / len(Alunos)
print("\nA Média De Notas Dos Alunos É:",med)
