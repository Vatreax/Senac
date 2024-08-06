salar = float(input("Digite Seu Salário: R$"))
i = 0
ano = 0
porcentagem = 1.5
total = 0

while i < 29:
    i += 1
    r = porcentagem / 100
    print(f"Porcentagem:", r)
    re = 1000 * r
    porcentagem = porcentagem * 2
    total = salar + re
    print("\nO Aumento Salárial em ", (ano + 1996)," : R$", total,"\n")
    ano += 1