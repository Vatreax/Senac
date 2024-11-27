const errorSpan = document.querySelector('.span-erro');
const successSpan = document.querySelector('.span-deu-certo');

const npu_1parte = /^({0-9}{7}\-[0-9]{2}\.{0-9}{4}\$/;
const npu_2parte = /^({0-9}{1,3}\$/;
const npu_3parte = /^({0-9}{4}\$/;

function digitado(index){
    spans[index].style.display = 'block',
    spans[index].style.color = red
}

function removeError(index){
    spans[index].style.display = 'none';
}

function npuValidate(){
    if (npu.test(inputs[0].value)) {
    removeError(0);
}
    else{
        setError(0);
    }
}