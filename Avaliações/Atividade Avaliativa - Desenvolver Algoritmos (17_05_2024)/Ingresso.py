meia = 2.50
ingre = 5
saldo = 0
quant1 = 0
quant2 = 0

entrada = "1"
saida = "0"

while entrada != saida:
    print("""
+========+============+=========+
| CÓDIGO |  INGRESSO  |  PREÇO  |
|--------|------------|---------|
|  201   |  Inteira   | R$ 5,00 |
|  202   |  Meia      | R$ 2,50 |
+========+============+=========+
""")

    code = input("Digite o Código do ingresso que deseja comprar: ")

    if code == "201":
        saldo += ingre
        quant1 += 1
        print(f"\nValor Total: R$ {saldo}\n")

    elif code == "202":
        code_uso = input("\nDigite o Código de Uso da Carteirinha: ")
        if len(code_uso) == 8:
            saldo += meia
            quant2 += 1
            print(f"\nValor Total: R$ {saldo}\n")
        else:
            print("\nCódigo Invalido\n")

    entrada = input("\nDigite QUALQUER tecla para - CONTINUAR Comprando\nDigite 0 para - PARAR\n -")

print(f"""

Saldo da Compra  : R${saldo}
Meia Entrada     : {quant2}
Ingressos Inteira: {quant1}
Ingressos Totais : {quant1+quant2}

""")