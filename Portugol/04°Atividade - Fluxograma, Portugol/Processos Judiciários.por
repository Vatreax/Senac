programa {
  funcao inicio() {

    cadeia sair

    inteiro abril
    inteiro maio
    inteiro junho
    inteiro julho
    inteiro agosto
    inteiro setembro
    inteiro mes


    abril = 5
    maio = 12
    junho = 21
    julho = 1
    agosto = 9
    setembro = 6

    escreva("\n\n___________Controle de Processos Judici�rios___________\n")
    escreva("\nQual m�s voc� deseja consultar de 4 a 9: ")
    leia(mes)

    se(mes<4 ou mes>9){
      escreva("mes invalido")
    } senao{
      se(mes==4){
        escreva("O n�mero de processos em Abril: ", abril)
      } se(mes==5){
        escreva("O n�mero de processos em maio: ", maio)
      } se(mes==6){
        escreva("O n�mero de processos em junho: ", junho)
      } se(mes==7){
        escreva("O n�mero de processos em julho: ", julho)
      } se(mes==8){
        escreva("O n�mero de processos em agosto: ", agosto)
      } se(mes==9){
      escreva("O n�mero de processos em setembro: ", setembro)
      }
    }

    
    }

  }
}
