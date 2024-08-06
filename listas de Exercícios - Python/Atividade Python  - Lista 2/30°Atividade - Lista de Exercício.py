n1 = float(input("Preço do Produto: R$"))
print("""

    """)

i= int(input("""Qual Estado Deseja Transportar:
                 
    1 - Minas Gerais (MG)
    2 - São Paulo (SP)
    3 - Rio de Janeiro (RJ)
    4 - Mato Grosso do Sul (MS)
                       
    - """))


if i == 1:
    re = n1 * (7/100)
    imp = n1 + re
    rounded = round(imp,2)
    print(f"""
          Minas Gerais (MG)
          Acréscimo do Imposto: R${rounded}
""")

elif i == 2:
    re = n1 * (12/100)
    imp = n1 + re
    rounded = round(imp,2)
    print(f"""
          São Paulo (SP)
          Acréscimo do Imposto: R${rounded}
""")

elif i == 3:
    re = n1 * (15/100)
    imp = n1 + re
    rounded = round(imp,2)
    print(f"""
          Rio de Janeiro (RJ)
          Acréscimo do Imposto: R${rounded}
""")
    
elif i == 4:
    re = n1 * (8/100)
    imp = n1 + re
    rounded = round(imp,2)
    print(f"""
          Mato Grosso do Sul (MS)
          Acréscimo do Imposto: R${rounded}
""")

elif i <= 0 or i >= 5:
    print("\nOpção Incorreta")