entrada = "S"
saida = "0"

lista_nome = []
lista_altura = []
lista_peso = []
contador = 0


while entrada != saida:
    nome = input("\nSeu Nome: ")
    lista_nome.append(nome)

    altura = float(input("Sua Altura: "))
    lista_altura.append(altura)

    peso = float(input("Seu Peso: "))
    lista_peso.append(peso)
    contador += 1
    
    entrada = input("""Deseja Continuar
    
    Aperte qualquer tecla para CONTINUAR
                    
    Digite [ 0 ] para Parar
                    
    - """)

lista1 = [float(+i) for i in lista_altura]
lista2 = [float(+i) for i in lista_peso]

Re1 = sum(lista1) /contador
Re2 = sum(lista2) /contador

print(f"""
-----------------------------------------------

A média da altura: 
{Re1}

A média de peso: 
{Re2}

-----------------------------------------------
""")

print(f"""
O maior peso:
{max(lista_peso)}
""")

print(f"""
O menor peso:  
{min(lista_peso)}
""")

print(f"""
A maior altura: 
{max(lista_altura)}
""")

print(f"""
A menor altura: 
{min(lista_altura)}

""")