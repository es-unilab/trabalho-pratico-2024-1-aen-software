const campoSenha = document.querySelector("#campoSenha")
const botaoMostrarSenha = document.querySelector("#botaoMostrarSenha ")
const legenda = document.querySelector(".legenda")

botaoMostrarSenha.addEventListener("change", function(){
    const estadoAtualDoCampoDeSenha = campoSenha.getAttribute("type") === "password" ? "text": "password";

    campoSenha.setAttribute("type",estadoAtualDoCampoDeSenha);
    legenda.ennerHTML= estadoAtualDoCampoDeSenha === "password" ? "mostrar" : "ocultar";
});
