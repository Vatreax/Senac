n1 = int(input("\nQuantos Anos Você Tem: "))
n2 = int(input("Quantos Anos Você Trabalhou: "))

if n1 >= 65:
    print("\nVocê Pode se Aposentar, Contate o INSS Para Mais Detalhes. <3\n")

elif n2 >= 30:
    print("\nVocê Pode se Aposentar, Contate o INSS Para Mais Detalhes. <3 <3\n")

elif n1 >= 60 and n2 >= 25:
    print("\nVocê Pode se Aposentar, Contate o INSS Para Mais Detalhes. <3 <3 <3\n")

else:
    print("\nVocê Não Pode se Aposentar.\n")