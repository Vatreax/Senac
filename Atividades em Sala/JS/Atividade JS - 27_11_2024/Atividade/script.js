function validarInput() {
  const digite = document.getElementById('digite');
  const messageSpan = document.getElementById('message');
  
  const npu = /^\d{7}-\d{1}\.\d{2}\.\d{4}$/;

  const value = digite.value;
  
  if (npu.test(value)) {
    messageSpan.textContent = 'Valor válido!';
    messageSpan.classList.remove('message');
    messageSpan.classList.add('valid');
  } else {
    messageSpan.textContent = 'Valor inválido!';
    messageSpan.classList.remove('valid');
    messageSpan.classList.add('message');
  }
}
