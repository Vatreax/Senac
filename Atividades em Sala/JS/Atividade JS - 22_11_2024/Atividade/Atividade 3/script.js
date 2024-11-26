var seu_dinheiro = window.prompt("Quantos Reais Você Possui? ")
var usd = 5.82
var cotacion = seu_dinheiro / (1 * usd)

window.alert("Seu Dinheiro: R$" + seu_dinheiro + "\nValor do Dolar com Relação ao Real: R$" + usd + "\nValor em Dolares: " + cotacion.toFixed(2))