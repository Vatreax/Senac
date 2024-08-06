print("""
------------------------------
| ESTACIONAMENTO DO SHOPPING |
------------------------------
""")

Tempo = int(input("Quantos Minutos o Usuário Vai Utilizar o Estacionamento: "))
valor_hora = float(9.00)

if Tempo >= 60:
    r = valor_hora
    print("Valor a Ser Cobrado: R$", r)

elif Tempo >= 120:
    r = valor_hora + 1.50
    print("Valor a Ser Cobrado: R$", r)

elif Tempo <= 15:
    r = 0
    print("Valor a Ser Cobrado: R$", r)