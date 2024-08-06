class Car:
    def __init__(self,marca,carroceria,rodas,passageiros,peso,preço_fabrica,eixo,performance,propulsão):
        self.marca = marca
        self.propulsão = propulsão
        self.performance = performance
        self.carroceria = carroceria
        self.rodas = rodas
        self.passageiros = passageiros
        self.peso = peso
        self.preço_fabrica = preço_fabrica
        self.eixo = eixo

class Habilitation(Car):
    def __init__(self, marca,carroceria, rodas, passageiros, peso, preço_fabrica, eixo, propulsão, performance, habilitation,nome):
        super().__init__(marca, carroceria, rodas, passageiros, peso, preço_fabrica, eixo, performance, propulsão)
        self.habilitation = habilitation
        self.nome = nome

veiculos = {
    #1° Veículo
    "Aurora 122c": Habilitation (nome= "Aurora 122c",marca= "Ferrari",propulsão= "Gasolina",performance= 680,carroceria="Sedan Esportivo",rodas=4,passageiros=4,peso=1500,preço_fabrica=180000,eixo="Tração Dianteira",habilitation="B"),
    
    #2° Veículo
    "Lamborghini Aventador": Habilitation(nome= "Lamborghini Aventador",marca= "Lamborghini",propulsão= "Gasolina",performance=730,carroceria= "Coupé",rodas= 4,passageiros= 2,peso= 1575,preço_fabrica= 2000000,eixo= "Tração nas Quatro Rodas",habilitation= "B"),
    
    #3°Veiculo
    "Track T-800": Habilitation(nome= "Track T-800",marca= "Track",propulsão= "Diesel",performance=30,carroceria= "Moto",rodas= 2,passageiros= 1,peso= 180,preço_fabrica= 50000,eixo= "Tração Traseira",habilitation= "A"),
    
    # 4° Veículo
    "Toyota Corolla": Habilitation(nome= "Toyota Corolla",marca= "Toyota",propulsão= "Gasolina",performance= 140,carroceria= "Sedan",rodas= 4,passageiros= 5,peso= 1300,preço_fabrica= 230000,eixo= "Tração Dianteira",habilitation= "B"),

    # 5° Veículo
    "Ducati Panigale V4": Habilitation(nome= "Ducati Panigale V4",marca= "Ducati",propulsão= "Gasolina",performance= 314,carroceria= "Moto Esportiva",rodas= 2,passageiros= 2,peso= 198,preço_fabrica= 250000,eixo= "Tração Traseira",habilitation= "A"),
    
    # 6° Veículo
    "Chevrolet Silverado": Habilitation(nome= "Chevrolet Silverado",marca= "Chevrolet",propulsão= "Gasolina",performance= 355 ,carroceria= "Caminhonete",rodas= 4,passageiros= 5,peso= 2328,preço_fabrica= 400000,eixo= "Tração Traseira",habilitation= "C"),
    
    # 7° Veículo
    "BMW 3 Series": Habilitation(nome= "BMW 3 Series",marca= "BMW",propulsão= "Gasolina",performance= 258,carroceria= "Sedan",rodas= 4,passageiros= 5,peso= 1555,preço_fabrica= 450000,eixo= "Tração Traseira",habilitation= "B"),
    
    # 8° Veículo
    "Kawasaki Ninja 400": Habilitation(nome= "Kawasaki Ninja 400",marca= "Kawasaki",propulsão= "Gasolina",performance= 49,carroceria= "Moto Esportiva",rodas= 2,passageiros= 2,peso= 168,preço_fabrica= 60000,eixo= "Tração Traseira",habilitation= "A"),
    
    # 9° Veículo
    "Harley-Davidson LiveWire": Habilitation(nome= "Harley-Davidson LiveWire",marca= "Harley-Davidson",propulsão= "Elétrica",performance= 305,carroceria= "Moto",rodas= 2,passageiros= 1,peso= 249,preço_fabrica= 95000,eixo= "Tração Traseira",habilitation= "A"),

    # 10° Veículo
    "Porsche 911 Carrera": Habilitation(nome= "Porsche 911 Carrera",marca= "Porsche",propulsão= "Gasolina",performance= 385,carroceria= "Coupé Esportivo",rodas= 4,passageiros= 4,peso= 1440,preço_fabrica= 900000,eixo= "Tração Traseira",habilitation= "B"),

    # 11° Veículo
    "Honda CR-V": Habilitation (nome= "Honda CR-V",marca= "Honda",propulsão= "Gasolina",performance= 190,carroceria= "SUV",rodas= 4,passageiros= 5,peso= 1600,preço_fabrica= 300000,eixo= "Tração Integral",habilitation= "C"),

    # 12° Veículo
    "Yamaha YZF-R6": Habilitation(nome= "Yamaha YZF-R6",marca= "Yamaha",propulsão= "Gasolina",performance= 120,carroceria= "Moto Esportiva",rodas= 2,passageiros= 2,peso= 190,preço_fabrica= 120000,eixo= "Tração Traseira",habilitation= "A"),

    # 13° Veículo
    "Ram 1500": Habilitation(nome= "Ram 1500",marca= "Ram",propulsão= "Gasolina",performance= 395,carroceria= "Picape",rodas= 4,passageiros= 5,peso= 2320,preço_fabrica= 350000,eixo= "Tração Traseira",habilitation= "C"),

    # 14° Veículo
    "Tesla Cybertruck": Habilitation(nome= "Tesla Cybertruck",marca= "Tesla",propulsão= "Elétrica",performance= 700,carroceria= "Picape",rodas= 4,passageiros= 6,peso= 2500,preço_fabrica= 400000,eixo= "Tração nas Quatro Rodas",habilitation= "B"),

    # 15° Veículo
    "Indian Scout Sixty": Habilitation(nome= "Indian Scout Sixty",marca= "Indian",propulsão= "Gasolina",performance= 78,carroceria= "Moto Cruiser",rodas= 2,passageiros= 2,peso= 254,preço_fabrica= 90000,eixo= "Tração Traseira",habilitation= "A"),

    # 16° Veículo
    "Volkswagen Golf": Habilitation(nome= "Volkswagen Golf",marca= "Volkswagen",propulsão= "Gasolina",performance= 150,carroceria= "Hatchback",rodas= 4,passageiros= 5,peso= 1316,preço_fabrica= 230000,eixo= "Tração Dianteira",habilitation= "B"),

    # 17° Veículo
    "Tesla Model 3": Habilitation(nome= "Tesla Model 3",marca= "Tesla",propulsão= "Elétrico",performance= 283,carroceria= "Sedan",rodas= 4,passageiros= 5,peso= 1620,preço_fabrica= 400000,eixo= "Tração Traseira",habilitation= "C"),

    # 18° Veículo
    "Ford F-150": Habilitation(nome= "Ford F-150",marca= "Ford",propulsão= "Gasolina",performance= 375,carroceria= "Picape",rodas= 4,passageiros= 5,peso= 2045,preço_fabrica= 350000,eixo= "Tração Traseira",habilitation= "C"),

    # 19° Veículo
    "Nissan Leaf": Habilitation(nome= "Nissan Leaf",marca= "Nissan",propulsão= "Elétrico",performance= 150,carroceria= "Hatchback",rodas= 4,passageiros= 5,peso= 1490,preço_fabrica= 180000,eixo= "Tração Dianteira",habilitation= "C"),

    # 20° Veículo
    "Tesla Model S": Habilitation(nome= "Tesla Model S",marca= "Tesla",propulsão= "Elétrico",performance= 510,carroceria= "Sedan",rodas= 4,passageiros= 5,peso= 2108,preço_fabrica= 500000,eixo= "Tração Integral",habilitation= "B"),

    # 21° Veículo
    "Chevrolet Camaro": Habilitation(nome= "Chevrolet Camaro",marca= "Chevrolet",propulsão= "Gasolina",performance= 650,carroceria= "Coupé Esportivo",rodas= 4,passageiros= 4,peso= 1800,preço_fabrica= 300000,eixo= "Tração Traseira",habilitation= "B"),

    # 22° Veículo
    "BMW X5": Habilitation(nome= "BMW X5",marca= "BMW",propulsão= "Diesel",performance= 400,carroceria= "SUV",rodas= 4,passageiros= 5,peso= 2200,preço_fabrica= 550000,eixo= "Tração Integral",habilitation= "C"),

    # 23° Veículo
    "Harley-Davidson Fat Boy": Habilitation(nome= "Harley-Davidson Fat Boy",marca= "Harley-Davidson",propulsão= "Gasolina",performance= 65,carroceria= "Moto Cruiser",rodas= 2,passageiros= 2,peso= 330,preço_fabrica= 120000,eixo= "Tração Traseira",habilitation= "A"),

    # 24° Veículo
    "Toyota Hilux": Habilitation(nome= "Toyota Hilux",marca= "Toyota",propulsão= "Diesel",performance= 177,carroceria= "Caminhonete",rodas= 4,passageiros= 5,peso= 2000,preço_fabrica= 280000,eixo= "Tração nas Quatro Rodas",habilitation= "C"),

    # 25° Veículo
    "Audi RS7": Habilitation(nome= "Audi RS7",marca= "Audi",propulsão= "Gasolina",performance= 600,carroceria= "Sedan Esportivo",rodas= 4,passageiros= 5,peso= 1950,preço_fabrica= 600000,eixo= "Tração Integral",habilitation= "B"),

    # 26° Veículo
    "Kawasaki Vulcan S": Habilitation(nome= "Kawasaki Vulcan S",marca= "Kawasaki",propulsão= "Gasolina",performance= 61,carroceria= "Moto Custom",rodas= 2,passageiros= 2,peso= 226,preço_fabrica= 45000,eixo= "Tração Traseira",habilitation= "A"),

    # 27° Veículo
    "Ford Ranger": Habilitation(nome= "Ford Ranger",marca= "Ford",propulsão= "Diesel",performance= 200,carroceria= "Caminhonete",rodas= 4,passageiros= 5,peso= 2200,preço_fabrica= 320000,eixo= "Tração nas Quatro Rodas",habilitation= "C"),

    # 28° Veículo
    "Mercedes-Benz GLC": Habilitation(nome= "Mercedes-Benz GLC",marca= "Mercedes-Benz",propulsão= "Gasolina",performance= 258,carroceria= "SUV",rodas= 4,passageiros= 5,peso= 1800,preço_fabrica= 450000,eixo= "Tração Integral",habilitation= "C"),

    # 29° Veículo
    "Honda CB500X": Habilitation(nome= "Honda CB500X",marca= "Honda",propulsão= "Gasolina",performance= 48,carroceria= "Moto Adventure",rodas= 2,passageiros= 2,peso= 196,preço_fabrica= 35000,eixo= "Tração Traseira",habilitation= "A"),

    # 30° Veículo
    "Jeep Compass": Habilitation(nome= "Jeep Compass",marca= "Jeep",propulsão= "Flex",performance= 170,carroceria= "SUV",rodas= 4,passageiros= 5,peso= 1500,preço_fabrica= 100000,eixo= "Tração nas Quatro Rodas",habilitation= "B"),

    # 31° Veículo
    "Mitsubishi L200 Triton": Habilitation(nome= "Mitsubishi L200 Triton",marca= "Mitsubishi",propulsão= "Diesel",performance= 190,carroceria= "Caminhonete",rodas= 4,passageiros= 5,peso= 2100,preço_fabrica= 300000,eixo= "Tração nas Quatro Rodas",habilitation= "C"),

    # 32° Veículo
    "Yamaha MT-07": Habilitation(nome= "Yamaha MT-07",marca= "Yamaha",propulsão= "Gasolina",performance= 74,carroceria= "Moto Naked",rodas= 2,passageiros= 2,peso= 182,preço_fabrica= 40000,eixo= "Tração Traseira",habilitation= "A"),

    # 33° Veículo
    "Hyundai Santa Fe": Habilitation(nome= "Hyundai Santa Fe",marca= "Hyundai",propulsão= "Diesel",performance= 200,carroceria= "SUV",rodas= 4,passageiros= 7,peso= 1900,preço_fabrica= 280000,eixo= "Tração Integral",habilitation= "C"),

    # 34° Veículo
    "Suzuki Jimny": Habilitation(nome= "Suzuki Jimny",marca= "Suzuki",propulsão= "Gasolina",performance= 102,carroceria= "SUV Compacto",rodas= 4,passageiros= 4,peso= 1100,preço_fabrica= 80000,eixo= "Tração nas Quatro Rodas",habilitation= "B"),

    # 35° Veículo
    "Ducati Multistrada 950": Habilitation(nome= "Ducati Multistrada 950",marca= "Ducati",propulsão= "Gasolina",performance= 313,carroceria= "Moto Adventure",rodas= 2,passageiros= 2,peso= 229,preço_fabrica= 90000,eixo= "Tração Traseira",habilitation= "A"),
    
    # 36° Veículo
    "Zero SR/F": Habilitation(nome= "Zero SR/F",marca= "Zero Motorcycles",propulsão= "Elétrica",performance= 110,carroceria= "Moto Esportiva",rodas= 2,passageiros= 2,peso= 220,preço_fabrica= 90000,eixo= "Tração Traseira",habilitation= "A")
    }

def da_uma_printada(veiculo):

    print(f"""-------------------------------------\n
~~~ {veiculo.nome} ~~~\n
Marca: {veiculo.marca}
Propulsão: {veiculo.propulsão}
Nivél de Performance: {veiculo.performance} Cv
Carroceria: {veiculo.carroceria}
Rodas: {veiculo.rodas}
Passageiros: {veiculo.passageiros}
Peso: {veiculo.peso} Kg
Preço de Fábrica: R${veiculo.preço_fabrica:.2f}
Eixo: {veiculo.eixo}
Habilitação Necessária: {veiculo.habilitation}""")



print("""
Bom dia, Boa Tarde ou Boa Noite!
Está a procura do seu Veículo ideal?
estamos aqui para ajudar.

Primeiro responda nossos Questionários:
\n""")

while True:
    question3= input("""
1) Qual tipo de véiculo você tem preferência?
    |1| Moto
    |2| Sedan / Sedan Esportivo
    |3| Caminhonete / Picape
    |4| Coupé / Coupé Esportivo
    |5| Hatchback
    |6| SUV
    |7| Sem Preferência
- """).capitalize()

    filtro3= []

    if question3 == "1":
        for chave3, veiculo3 in veiculos.items():
            if veiculo3.rodas > 2:
                filtro3.append(chave3)
        print("\n-- Resposta Registrada --\n")
        break

    elif question3 == "2":
        for chave3, veiculo3 in veiculos.items():
            if veiculo3.carroceria != "Sedan" and veiculo3.carroceria != "Sedan Esportivo":
                filtro3.append(chave3)
        print("\n-- Resposta Registrada --\n")
        break

    elif question3 == "3":
        for chave3, veiculo3 in veiculos.items():
            if veiculo3.carroceria != "Caminhonete" and veiculo3.carroceria != "Picape":
                filtro3.append(chave3)
        print("\n-- Resposta Registrada --\n")
        break

    elif question3 == "4":
        for chave3, veiculo3 in veiculos.items():
            if veiculo3.carroceria != "Coupé Esportivo" and veiculo3.carroceria != "Coupé":
                filtro3.append(chave3)
        print("\n-- Resposta Registrada --\n")
        break

    elif question3 == "5":
        for chave3, veiculo3 in veiculos.items():
            if veiculo3.carroceria != "Hatchback":
                filtro3.append(chave3)
        print("\n-- Resposta Registrada --\n")
        break

    elif question3 == "6":
        for chave3, veiculo3 in veiculos.items():
            if veiculo3.carroceria != "SUV":
                filtro3.append(chave3)
        print("\n-- Resposta Registrada --\n")
        break

    elif question3 == "7":
        print("\n-- Resposta Registrada --\n")
        break
    else:
        print("\n+=================+\n|Resposta Invalida|\n+=================+\n")
        continue

for carro3 in filtro3:
    del veiculos[carro3]

# Apague os Comentários Para Ver o Filtro Funcionando
#for e,cont3  in veiculos.items():
#    da_uma_printada(cont3)
#    print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    question2= input("""
2) Tipos de propulsão:

    |1| Combustão (Diesel/Gasolina)
    |2| Elétrico
    |3| Sem preferência

- """).capitalize()

    filtro2 = []

    if question2 == "1":
        for chave2, veiculo2 in veiculos.items():
            if veiculo2.propulsão != "Gasolina" and veiculo2.propulsão != "Diesel":
                filtro2.append(chave2)

        print("\n-- Resposta Registrada --\n")
        break

    elif question2 == "2":
        for chave2, veiculo2 in veiculos.items():
            if veiculo2.propulsão != "Elétrico":
                filtro2.append(chave2)

        print("\n-- Resposta Registrada --\n")
        break

    elif question2 == "3":
        print("\n-- Resposta Registrada --\n")
        break

    else:
        print("\n+=================+\n|Resposta Invalida|\n+=================+\n")

for carro2 in filtro2:
    del veiculos[carro2]

# Apague os Comentários Para Ver o Filtro Funcionando
#for e,cont2  in veiculos.items():
#    da_uma_printada(cont2)
#    print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    question1= input("""
3) Estilo de Vida:

    |1| Você prefere veículos que ofereçam alta performance
    |2| Você prefere veículos de passeio

- """).capitalize()

    filtro = []

    if question1 == "1":
            for chave, veiculo in veiculos.items():
                if veiculo.performance < 300:
                    filtro.append(chave)
            print("\n-- Resposta Registrada --\n")
            break

    elif question1 == "2":
        for chave, veiculo in veiculos.items():
            if veiculo.performance >= 300:
                filtro.append(chave)
        print("\n-- Resposta Registrada --\n")
        break

    else:
        print("\n+=================+\n|Resposta Invalida|\n+=================+\n")
        continue
for carro in filtro:
    del veiculos[carro]

print("\nVeículo(s) Encontrado(s):\n")
for b,cont in veiculos.items():
    da_uma_printada(cont)
    print()