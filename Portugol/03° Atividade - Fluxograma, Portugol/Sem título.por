programa {
  funcao inicio() {
    inteiro estq,sant,ent,sd


    escreva("\n\n\n Estoque Atual\n\n")

    escreva("Quantidade do Saldo em Estoque: ")
    leia(ent)

    escreva("Quantidade de Compras do Mês: ")
    leia(sant)

    escreva("Quantidade de Vendas: ")
    leia(sd)

  estq=sant+ent-sd
  escreva("\n A Quantidade Atual em Estoque: ",estq)
  }
}
