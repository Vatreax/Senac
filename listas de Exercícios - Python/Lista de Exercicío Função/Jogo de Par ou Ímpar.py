import random
import sys
def fun(num):
    sono = random.randint(1,sys.maxsize)
    print(f"Número Aleatório: {sono}")
    soma = sono + num
    if soma % 2 == 0:
        print(f"\nO número {soma} é par ;)")
    else:
        print(f"\nO número {soma} é Ímpar *-*")
    
num = int(input("Digita um Número ai: "))
fun(num)