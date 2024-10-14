print("\n -Preencha os seguintes dados: \n")
 
nome = input("Nome: ")
idade = int(input("Idade: "))
salario = float(input("Seu salário: "))
sexo = input("Seu sexo: (M/F) ")
   
while len(nome) < 3:
    print("Nome invalido! Digite novamente.")
    nome = input("Nome: ")
 
while idade <= 0 and idade >= 150:
    print("Idade invalida! Digite novamente.")
    idade = int(input("Idade: "))
   
while salario < 0:
    print("Salario invalido! Digite novamente.")
    salario = float(input("Seu salario: "))
 
while sexo != "M" and sexo != "m" and sexo != "F" and sexo != "f":
    print("Sexo invalido! Digite novamente.")
    sexo = input("Seu sexo: (M/F) ")
       
if sexo == "M" or sexo == "m":
    sexo = "Masculino"
       
if sexo == "F" or sexo == "f":
    sexo = "Feminino"
   
 
print(f"""
============ Dados Cadastrados ============
| Nome:    | {nome}                         
| Idade:   | {idade} anos                    
| Salário: | R${salario}                     
| Sexo:    | {sexo}                            
===========================================
""")