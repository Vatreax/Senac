def fun(arg1,arg2,arg3):
    arg1 = float(input("1°Lado: "))
    arg2 = float(input("2°Lado: "))
    arg3 = float(input("3°Lado: "))
    re = arg1 - arg2
    if arg1 + arg2 < arg3 and arg3 + arg1 < arg2 and arg3 + arg2 < arg1:
        print("Não é um Triângulo!!! >:(\nTenha um Bom Dia <3")
    elif arg3 == arg2 or arg2 == arg1 or arg3 == arg1:
        print("É um Triângulo, Meu Nobre :)")
    elif arg1 > (arg2-arg3) or arg2 > (arg1-arg3) or arg3 > (arg1-arg2):
        print("Não é um Triângulo!!! >:(\nTenha um Bom Dia <3")
    else:
        print("É um Triângulo, Meu Nobre :)")
fun(1,2,3)