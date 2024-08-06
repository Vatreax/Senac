def fun(n1):
    n1 = int(input("Digite um Número ai: "))
    soma = 0
    for div in range(1,n1):
        if n1 % div == 0:
            soma = soma + div 
    if n1 == soma:
        print(f"O número é Perfeito :)")
    else:
        print("Não é Pre-feito ;-;")
fun(1)