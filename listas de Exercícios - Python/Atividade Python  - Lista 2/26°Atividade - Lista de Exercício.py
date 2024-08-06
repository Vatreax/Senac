ano = int(input("\nDigite um Ano: "))

bissexto1 = ano % 2

if bissexto1 == 0:
    print(f"\nO Ano {ano}, é um Ano Bissexto.\n")

else :
    print(f"\nO Ano {ano}, Não é um Ano Bissexto.\n")
