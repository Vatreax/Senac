prod = float(input("Preço do Produto: R$"))

if prod < 50:
    re1 = prod * (45/100)
    re2 = prod + re1
    print("\nO preço de revenda: R$", re2,"\n")
elif prod >= 50:
    re3 = prod * (30/100)
    re4 = prod - re3
    print("Lucro a ser obtido: R$", re4,"\n")
else:
    print("Se Quiser Sim.")