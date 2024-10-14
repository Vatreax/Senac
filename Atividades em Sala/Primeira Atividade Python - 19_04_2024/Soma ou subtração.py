N1= int(input("Digite o 1°Número Inteiro: "))
N2= int(input("Digite o 2°Número Inteiro: "))

R1 = N1 + N2
R2 = N1 - N2

F = float(input("""
           Qual operação você deseja:
           1 - Soma
           2 - Subtração
           """))

if(F<=0 and F<2):
    print("Erro")
if(F==1):
    print("O resultado é: ", R1)
if(F==2):
    print("O resultado é: ", R2)    
        