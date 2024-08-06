prod = ["Sorvete - Alimento: Frio - Código 1","Escova de Dente - Higiene: Bocal - Código 2", "Frigideira - Item: Cozinha - Código 3","Tesoura - Item: Escritório - Código 4 "]
quanti = [10,10,10,10]
preço = [10.50,6.25,39.99,4.15]

for i in prod:
        print(i)
n = 0
for a in preço:
        n+=1
        print(f"Preço do Produto {n}:",a)

m = 0
while m < 4:
        m = m + 1
        print(m)
        sele = int(input("\nDigite o Produto Desejado: "))

        print(prod[sele-1],"\nPreço: R$",preço[sele-1])

        carrinho = 0
        carrinho =+ preço[sele-1]
        print("Seu Carrinho: ", carrinho)


dinheiro = float(input("\nSeu Dinheiro: "))

saldo = dinheiro - carrinho

print("Seu Saldo: ", saldo)

