import math
def fun(Lado1,Lado2,Hipo):
    Lado1 = float(input("1°Lado: "))
    Lado2 = float(input("2°Lado: "))
    Hipo = ((Lado1**2) + (Lado2**2))
    print("Hipotenusa:", math.sqrt((Hipo)))
fun(1,2,3)