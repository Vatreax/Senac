const input1 = document.querySelectorAll('input');
const input2 = document.querySelector('.input2');
const input3 = document.querySelector('.input3');

const npu_1parte = /^({0-9}{7}\-[0-9]{2}\.{0-9}{4}$/;
const npu_2parte = /^({0-9}{1,3}$/;
const npu_3parte = /^({0-9}{4}$/;


function digitado(){
    if (npu_1parte.test(input1.value)) {
        removeError();
    } else{
        setError();
    }
    if (npu_2parte.test(input2.value)) {
        removeError();
    } else{
        setError();
    }
    if (npu_3parte.test(input3.value)) {
        removeError();
    } else{
        setError();
    }
}

function setError() {
    errorSpan.style.display = 'block';
    errorSpan.style.color = 'red';
    successSpan.style.display = 'none';
}
 
function removeError() {
    errorSpan.style.display = 'none';
    successSpan.style.display = 'block';
    successSpan.style.color = 'green'
}