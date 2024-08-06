n1 = int(input("Quanto Você Ganha Por Hora: "))
n2 = int(input("Horas Trabalhadas Por Mês: "))

sala_bruto = n1 * n2
imp  = sala_bruto * (11/100)
inss = sala_bruto * (8/100)
sind = sala_bruto * (5/100)
sala_liq   = (((sala_bruto - imp) - sind) - inss)

print(f"""

Salário Bruto    = R${sala_bruto}
Imposto de Renda = R${imp}
INSS             = R${sind}
Imposto Sindical = R${inss}

Salário Liquido  = R${sala_liq}

""")