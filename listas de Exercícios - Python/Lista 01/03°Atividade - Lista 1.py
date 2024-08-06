nome = input("Seu Nome: ")
idade = int(input("Sua Idade: "))
sala = float(input("Seu Salário: R$"))
sex = input("""
Defina Seu Sexo:
f - Feminino
m - Masculino
o - Outros    
- """)

sex = input("""
Defina Seu Sexo:
s - Solteiro
c - Casado
v - Viúvo  
d - Divorciado            
- """)

while len(nome) > 3:
    print("\nNome Validado")
    break

while idade >= 0 and idade <= 150:
    print("Idade Validada")
    break

while sala > 0 :
    print("Salário Validado")
    break

while sex == "f" or sex == "m" or sex == "o":
    print("Sexo Validado")
    break

while sex == "s" or sex == "c" or sex == "v" or sex == "d":
    print("Sexo Validado")
    break

else:
    print("\nDados Invalidos")