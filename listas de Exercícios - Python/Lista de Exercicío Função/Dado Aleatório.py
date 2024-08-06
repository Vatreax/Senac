import random
def fun(num):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    for i in range(num):
        listo = ["Lado 1","Lado 2","Lado 3","Lado 4","Lado 5","Lado 6"]
        lado_escolhido = random.choice(listo)

        if lado_escolhido == "Lado 1":
            a+=1
        elif lado_escolhido == "Lado 2":
            b+=1
        elif lado_escolhido == "Lado 3":
            c+=1
        elif lado_escolhido == "Lado 4":
            d+=1
        elif lado_escolhido == "Lado 5":
            e+=1
        elif lado_escolhido == "Lado 6":
            f+=1

        porcem1 = a/num
        porcem2 = b/num
        porcem3 = c/num
        porcem4 = d/num
        porcem5 = e/num
        porcem6 = f/num

    print(f"""
Número de vezes Lançadas: {a+b+c+d+e+f}
Vezes em que caiu o Lado 1: {round(porcem1*100,1)}%
Vezes em que caiu o Lado 2: {round(porcem2*100,1)}%
Vezes em que caiu o Lado 3: {round(porcem3*100,1)}%
Vezes em que caiu o Lado 4: {round(porcem4*100,1)}%
Vezes em que caiu o Lado 5: {round(porcem5*100,1)}%
Vezes em que caiu o Lado 6: {round(porcem6*100,1)}%
""")

fun(100)
fun(100000)
fun(1000000)