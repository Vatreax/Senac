print("""
      
===================    
|Números de 0 a 50|
===================
""")
n1 = float(input(" 1° Número: "))
n50 = []
n50.append(n1)
i = 1

while n1 > 0 and n1 < 50:
    i += 1
    n1 = float(input(f"\n {i}° Número: "))
    n50.append(n1)

print("\n\nNúmeros Entre 0 e 50: ", n50)