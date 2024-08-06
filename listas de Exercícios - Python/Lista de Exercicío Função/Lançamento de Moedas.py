import random
def fun(num):
    a = 0
    b = 0
    for i in range(num):
        listo = ["Cara","Coroa"]
        lado_escolhido = random.choice(listo)
        print(lado_escolhido)
        if lado_escolhido == "Cara":
            a+=1
        elif lado_escolhido == "Coroa":
            b+=1
        porcem1 = a/100
        porcem2 = b/100
        print(f"""
Número de vezes Lançadas: {a+b}
Vezes em que caiu Cara: {(porcem1*10),"%"} 
Vezes em que caiu Coroa: {(porcem2*10),"%"}
""")
fun(1000)