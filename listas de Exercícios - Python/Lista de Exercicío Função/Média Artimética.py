def fun(listo):
    i=0
    listo = []
    while True:
        i+=1.0
        listo.append(float(input(f"\n\nDigite uma Nota: ")))
        ent = input("""\nDigite:
|1|Adicionar Nota
|2|Terminar
- """)

        if ent == "2":
            break
    media = sum(listo)/i
    print(f"A Média é {round(media,2)}\n\n\nObs: Era só você ter usado uma Calculadora ao invés de um sistema ;-;")
fun(1)