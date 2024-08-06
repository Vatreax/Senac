impress = float(input("\nEmpréstimo a Ser Retirado: "))
salario = float(input("Seu Salário: "))

media = salario * (20/100)
print("Média de 20% do salario: ",media)

if impress > media:
    print("\nEmpréstimo Cancelada")
elif impress <= media:
    print("\nEmpréstimo Concebido")