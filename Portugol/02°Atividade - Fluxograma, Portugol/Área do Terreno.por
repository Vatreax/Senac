programa {
  funcao inicio() {
    real A, B, H
    leia(B,H)
    se(B!=H){
      A=B*H
      escreva("A �rea do terreno � = ", A)
    } se(B==H){
      A=B*H
      escreva("Os dados s�o de um quadrado")
    }
  }
}
