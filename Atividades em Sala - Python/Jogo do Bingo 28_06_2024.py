import random

roleta = []

def fun_roleta():
    global n1
    n1 = random.randint(1,75)
    print(f'\nNúmero Sorteado: {n1}\n')

def fun_cartela():
    global dicionario
    dicionario = {
    'B':[],
    'I':[],
    'N':[],
    'G':[],
    'O':[]
    }   

    while len(dicionario['B']) <= 5:
        num_random = random.randint (1,15)
        dicionario['B'].append(num_random)
            
    while len(dicionario['I'] ) <= 5:
        num_random = random.randint (15,30)
        dicionario['I'].append(num_random)

    while len(dicionario['N'] ) <= 5:
        num_random = random.randint (30,45)
        dicionario['N'].append(num_random)

    while len(dicionario['G'] ) <= 5:
        num_random = random.randint (45,60)
        dicionario['G'].append(num_random)

    while len(dicionario['O'] ) <= 5:
        num_random = random.randint (60,75)
        dicionario['O'].append(num_random)

def printa_com_meu_printe():
    print(dicionario)

def deu_erro_guys():
    print("""
+=-=-=-=-=-=-=-=-+
| Opção Invalida |
+=-=-=-=-=-=-=-=-+
""")

while True:
    op = input(f"""\n\
    ~-~ Bingo ~-~

    Operações:
    |1| Iniciar Jogo
    |2| Girar Roleta
    |3| Encerrar Sistema

    -""")
    
    if op == "3":
        print("Tenha um Bom Dia. (^-^)")
        break

    elif op == "2":
        fun_roleta()

    else:
        deu_erro_guys()

        while op == "1":
            fun_cartela()
            op2 = input("""
    |1| Começar
    |2| Visualizar Roleta
    |3| Cancelar
""")    

            if op2 == '2':
                printa_com_meu_printe()
            
            elif op2 == '3':
                break

            else:
                deu_erro_guys