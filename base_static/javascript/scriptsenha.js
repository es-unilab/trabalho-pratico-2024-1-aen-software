function mostrarSenha(){
    var inputSenha = document.getElementById('senha')
    var btnMostraSenha = document.getElementById('btn-senha')

    if(inputSenha.type === 'password'){
        inputSenha.setAttribute('type','text')
        btnMostraSenha.classList.replace('bi-eye-fill','bi-eye-slash-fill')
    }
    else {
        inputSenha.setAttribute('type','password')
        btnMostraSenha.classList.replace('bi-eye-slash-fill','bi-eye-fill')
    }
}