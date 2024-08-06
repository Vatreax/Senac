n1 = int(input("Digite Um Número: "))
n2 = int(input("Digite o Segundo Número: "))
list = []
for i in range(n1,n2):
    list.append(i)
print("A soma dos Intervalos: ", sum(list))