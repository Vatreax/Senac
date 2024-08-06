turn = input("""Em que turno você estuda?
    Digite
    M para Matutino
    V para Vespertino
    N para Noturno
             
 - """)

if turn == "M":
    print("\nBom Dia!")
elif turn == "V":
    print("\nBoa Tarde!")
elif turn == "N":
    print("\nBoa Noite!")
else:
    print("\nErro")