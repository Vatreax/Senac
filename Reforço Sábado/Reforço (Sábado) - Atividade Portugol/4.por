programa {
  funcao inicio() {
    inteiro dia, mes, ano
    cadeia cidade
    real graus

    escreva("\nA data de Hoje: \n")
    escreva("Dia - ")
    leia(dia)

    escreva("Mês - ")
    leia(mes)

    escreva("Ano - ")
    leia(ano)

    escreva("\nCidade: ")
    leia(cidade)

    escreva("\nQuantos Graus: ")
    leia(graus)

    escreva("\nHoje ", dia, "/", mes, "/", ano, " na cidade de ", cidade, " registra ", graus, " graus\n")
  }
}
