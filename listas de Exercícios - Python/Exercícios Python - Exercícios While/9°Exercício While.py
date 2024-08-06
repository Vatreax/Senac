entrada = "1"
saida = "0"
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
vot_n = 0
vot_b = 0

while entrada != saida:
    print("""

| N° Do Candidato |     CANDIDATO     |
|-----------------+-------------------|
|       1         |  James Bond       |
|       2         |  John Constantine |
|       3         |  J.J.Jameson      |
|       4         |  John Wick        |
|-----------------+-------------------|
""")
    codigo = input("""
Digite o Código do candidato que deseja Votar
                OU
    DIGITE 5 - Para Votar Nulo
    DIGITE 6 - Para Votar Branco
    - """)

    if codigo == "1":
        cand1 = cand1 + 1
        print("\nVóto Computado\n")

    elif codigo == "2":
        cand2 = cand2 + 1
        print("\nVóto Computado\n")

    elif codigo == "3":
        cand3 = cand3 + 1
        print("\nVóto Computado\n")

    elif codigo == "4":
        cand4 = cand4 + 1
        print("\nVóto Computado\n")

    elif codigo == "5":
        vot_n = vot_n + 1
        print("\nVóto Computado\n")

    elif codigo == "6":
        vot_b = vot_b + 1
        print("\nVóto Computado\n")
    
    else:
        print("\nNERRO - Número Incorreto\n")

    entrada = input("""Deseja Continuar Votando
    Aperte QUALQUER Tecla - Para CONTINUAR Votação
    Aperte a Tecla 0      - Para PARAR Votação
                    
    - """)

print(f"""
| N° Do Candidato |     CANDIDATO     | Quantidade de Votos
|       1         |  James Bond       |  {cand1}
|       2         |  John Constantine |  {cand2}
|       3         |  J.J.Jameson      |  {cand3}
|       4         |  John Wick        |  {cand4}

            Votos Nulos : {vot_n}
            Votos Brancos : {vot_b}
""")