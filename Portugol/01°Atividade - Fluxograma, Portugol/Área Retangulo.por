programa {
  funcao inicio() {
    real A, B, H
    leia(B,H)
    se(B!=H){
      A=B*H
      escreva("A área do retangulo é = ", A)
    } se(B==H){
      A=B*H
      escreva("A área do quadrado é = ", A)
    }
  }
}
