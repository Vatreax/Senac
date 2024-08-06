dias= ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo" ]
N1=int(input("Digite um número, meu nobre: " ))

if(N1>1 and N1<7):
    print("Hoje é: ", dias[N1-1])
