programa {
  funcao inicio() {
    real A, B, H
    leia(B,H)
    se(B!=H){
      A=B*H
      escreva("A área do terreno é = ", A)
    } se(B==H){
      A=B*H
      escreva("Os dados são de um quadrado")
    }
  }
}
