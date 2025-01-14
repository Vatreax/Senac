// /[a-z]/i.test("AZ")

// \d - Caracteres numéricos
// \s -Para corresponder ao próximo caractere com espaço em branco
// \D - Caracteres não numéricos

// + - uma ou mais ocorrências
// * - zero ou mais
// {n}: - Valor exato de elementos
// {n,m}: - Valor Minimo e Máximo
// ?: - Zero ou Uma ocorrência

// ^ - Inicio da String
// $ - Fim da String

// document.write(/[AZ])/i.test('AZ'));
// document.write("<br>")
// document.write(/love/i.test('LovE'));
// document.write("<br>")
// document.write(/[\bx]/.test('123x'));
// document.write("<br>")
// document.write(/\s/.test(' w'));

// document.write(/^\d{2}\/d{2}\/\d{4}$/.test('33/33/3333'))

// var dia = /^(0[1-9]|1[0-9]|[2[0-9]|3[0-1])$/;
// var mes = /^(0[1-9]|1[0-2])$/;
// var ano = /^\d{4}$/;

// var data = /^(0[1-9]|1[0-9]|3{0-1})\/(0[1-9]|1[0-2])\/\d{4}$/;
// document.write(data.test("22/04/2120"))
// document.write("<br>")

// var cpf = /^({0-9}{3}\.[0-9]{3}\.{0-9}{3}\-[0-9]{2})$/;
// document.write(cpf.test("957.877.555-55"))
// document.write("<br>")

// var email = /^[a-zA-Z09._%+-]+\@[a-zA-Z0-9.-]+\.[a-zA-Z.]{2,}$/;
// document.write(email.test("teste@teste.com"))
// document.write("<br><br>")

const inputs = document.querySelectorAll('.required');
const spans = document.querySelectorAll('.span-required');
const email = /^[a-zA-Z0-9._%+-]+@[az-A-Z0-9.-]+\.[a-zA-Z]{2,}$/

function setError(index){
    spans[index].style.display = 'block',
    spans[index].style.color = red
}

function removeError(index){
    spans[index].style.display = 'none';
}

function emailValidate(){
    if (email.test(inputs[0].value)) {
    removeError(0);
}
    else{
        setError(0);
    }
}