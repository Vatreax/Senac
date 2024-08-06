print("""
+==================+==============+==================+============+
| Salário Atual    | Reajuste (%) | Tempo de Serviço | Bônus      |
|------------------|--------------|------------------|------------|
| Até 500,00       |     25%      | Abaixo de 1 ano  | Sem bônus  |
|------------------|--------------|------------------|------------|
| Até 1000,00      |     20%      | De 1 a 3 anos    |  100,00    |
|------------------|--------------|------------------|------------|
| Até 1500,00      |     15%      | De 4 a 6 anos    |  200,00    |
|------------------|--------------|------------------|------------|
| Até 2000,00      |     10%      | De 7 a 10 anos   |  300,00    |
|------------------|--------------|------------------|------------|
| Acima de 2000,00 | Sem reajuste | Mais de 10 anos  |  500,00    |
+==================+==============+==================+============+
""")

serv = int(input("Em anos, Qual o Seu Tempo de Serviço? "))
sala = float(input("Seu Salario Atual: "))

if sala >= 500.00 and serv < 1:
    rea = sala * (25/100)
    total = sala + rea
    print(f"""
 Salario Atual = R${sala}
 Reajuste      = R${rea}
 Salario + Reajuste = R${total}
 Sem Direito ao Bônus (Faz o L)

""")
elif sala >= 1000.00 and serv >= 1 or serv <= 3:
    rea = sala * (20/100)
    total = sala + rea + 100.00
    print(f"""
 Salario Atual = R${sala}
 Reajuste      = R${rea}
 Bônus         = R$100.00
 Salario + Reajuste + Bônus = R${total}
 

""")
elif sala >= 1500 and serv > 4 or serv <= 6:
    rea = sala * (15/100)
    total = rea + sala + 200.00
    print(f"""
 Salario Atual = R${sala}
 Reajuste      = R${rea}
 Bônus         = R$200.00
 Salario + Reajuste + Bônus = R$

""")
elif sala == 2000 and serv > 10:
    rea = sala * (10/100)
    total = sala + rea + 300.00
    print(f"""
 Salario Atual = R${sala}
 Reajuste      = R${rea}
 Bônus         = R$300.00
 Total         = R%{total}
 
""")
if sala > 2000.00 and serv > 10:
    total = sala + 500.00
    print(f"""
 Salario Atual   = R${sala}
 Bônus           = R$500.00
 Salario + Bônus = R${total}
 Sem Reajuste (Faz o L)
 

""")

else:
    print("Dados Não Conferem Com a Tabela de Reajuste.")