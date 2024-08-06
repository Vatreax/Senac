nome = input("Nome: ")
idade = int(input("Idade: "))

if idade >= 5 and idade <= 12:
    print(f"""
+=------------------------------=+
|       CATEGORIA INFANTIL       
|        Nome: {nome}            
|       idade: {idade}           
+=------------------------------=+
""")
elif idade >= 12 and idade <= 17:
    print(f"""
+=------------------------------=+
|       CATEGORIA JUVENIL        
|        Nome: {nome}            
|       idade: {idade}           
+=------------------------------=+
""")

else:
    print(f"""
+=------------------------------=+
|       CATEGORIA SÊNIOR         
|        Nome: {nome}            
|       idade: {idade}           
+=------------------------------=+
""")
