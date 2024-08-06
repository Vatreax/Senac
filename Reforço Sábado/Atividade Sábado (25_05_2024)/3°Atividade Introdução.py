n1 = float(input("Digite o Seu Salário Atual: R$"))

if n1 < 500.00:
    porcem = n1 * (15/100)
    valor_total = n1 + porcem
    print(f"\nValor Atuallizado Pelo Reajuste: R${valor_total}")

elif n1 >= 500.00 and n1 <= 1000.00:
    porcem = n1 * (10/100)
    valor_total = n1 + porcem
    print(f"\nValor Atuallizado Pelo Reajuste: R${valor_total}")

elif n1 > 1000.00:
    porcem = n1 * (5/100)
    valor_total = n1 + porcem
    print(f"\nValor Atuallizado Pelo Reajuste: R${valor_total}")