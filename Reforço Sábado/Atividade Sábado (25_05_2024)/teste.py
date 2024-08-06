preço = [10.50,6.25,39.99,4.15]
print(preço)
n1 = float(input("Digite um número que deseja remover: "))

preço.remove(n1)
print(preço)

print(max(preço))
print(min(preço))
print(sum(preço))