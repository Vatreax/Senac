temp = int(input("\nQuantas Horas Trabalhadas (Máximo de 10 horas): "))
salario = temp * 40.50

if salario >= 2500:
    imp = salario * (11/100)
    salario_liq = salario - imp
    print("\nSalário Liquido: ", salario_liq)

else:
    print("Salário Liquido: ", salario)