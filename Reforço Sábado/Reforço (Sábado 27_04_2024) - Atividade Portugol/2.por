programa {
  funcao inicio() {

  cadeia entrada, saida, i
  real N1, N2, R1, R2, R3, R4
  entrada = "S"
  saida = "N"

  enquanto (entrada!=saida){

    escreva("--------------------")
    escreva("|Pseudo Calculadora|")
    escreva("--------------------")

    escreva("\ninsira o primeiro número: ")
    leia(N1)

    escreva("Insira o segundo número: ")
    leia(N2)

    escreva("\nQual operação deseja realizar: ", "\n1 - Soma", "\n2 - Subtração", "\n3 - Multiplicação ", "\n4 - Divisão", "\n- ")
    leia(i)

    R1 = N1 + N2
    R2 = N1 - N2
    R3 = N1 * N2
    R4 = N1 / N2
    
    se (i==1){
      escreva("\nO Resultado: ", R1, "\n")
    } 
    
    se (i==2){
      escreva("\nO Resultado: ", R2, "\n")
    }
    
     se (i==3){
      escreva("\nO Resultado: ", R3, "\n")

    } 
    
    se (i==4){
      escreva("\nO Resultado: ", R4, "\n")

    }
    
    senao se (i != 1 ou i != 2 ou i != 3 ou i != 4) {
      escreva("\nNúmero Invalido \n")

    }

    
    escreva("\nDeseja Continuar(S/N): ")
    leia(entrada)

  }  
  }
}