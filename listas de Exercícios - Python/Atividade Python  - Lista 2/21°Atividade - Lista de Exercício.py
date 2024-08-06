print("""
+================+
| Média de Notas |
+================+
""")

n1 = float(input("Nota do Trabalho de Laboratório: "))
n2 = float(input("Avaliação Semestral: "))
n3 = float(input("Exame Final: "))

Med = (n1+n2+n3*2) / 4

if Med <= 2.9 and Med >= 0:
    print(f"""      
    Aluno Reprovado
    Média: {Med}""")

elif Med >= 3 and Med <= 5.9:
    print(f"""      
    Aluno de Recuperação
    Média: {Med}""")

elif Med >= 6 and Med <= 10:
    print(f"""      
    Aluno Aprovado
    Média: {Med}""")

elif Med > 0 or Med > 10:
    print("Notas Incorretas")