entrada = "1"
saida = "0"

bat_s  = 10.00
bat_l  = 15.00
danone = 5.00
total  = 0

while entrada != saida:
    print("""
          
+===========+==================+===========+
|   CÓDIGO  |     PRODUTOS     |   PREÇO   |     
|-----------|------------------|-----------|
|    201    |  Bolacha Oreo    | R$ 10,00  |
|    202    |  Chocolate       | R$ 15,00  |
|    203    |  Danone          | R$  5,00  |
+===========+==================+===========+
          
""")

    código = input("Digite o Código de um dos Produtos: ")

    if código == "201":
            total = total + bat_s
            print("\nDinheiro a ser Debitado: R$", total,"\n")

    elif código == "202":
            total = total + bat_l
            print("\nDinheiro a ser Debitado: R$", total,"\n")

    elif código == "203":
            total = total + danone
            print("\nDinheiro a ser Debitado: R$", total,"\n")
            
    else:
          print("\nErro - Código Invalido\n")

    
    entrada = input("""
                    
Deseja Continuar Comprando?
Digite  qualquer tecla                - para CONTINUAR compra
Digite  a Técla  ----> [ 0 ] <----    - para PARAR compra

- """)

carteira = float(input("Seu Saldo: R$"))
saldo    = carteira - total 

if saldo > 0:
    print(f"""
          
Total de Troco: R${saldo}

""")

elif saldo == 0:
    print("\nCompra Realizada Com Sucesso")


elif saldo < 0:
    print(f"""
          
Você Não Tem Saldo Suficiente Para Realizar a Compra

""")