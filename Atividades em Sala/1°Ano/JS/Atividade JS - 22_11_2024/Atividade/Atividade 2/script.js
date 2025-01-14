var produto = window.prompt("Qual o nome do Produto:")
var quantidade = window.prompt("Quanto desse Produto deseja comprar:")
var price = window.prompt("O preço desse produto:")
var desconto = window.prompt("O desconto desejado:")

var valor_compra = quantidade * price
var valor_desconto = valor_compra * (desconto / 100)
var valor_total = valor_compra - valor_desconto

window.alert("O valor total da compra do produto " + produto + ": " + valor_total)
window.alert("Nome: " + produto+ "\nQuantidade:" + quantidade + "\nPreço:" + price + "\nDesconto: " + desconto)