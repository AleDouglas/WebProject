function toggleButton(){
    var toggleBtn = document.getElementsByClassName('menu')[0]
    var togglePosition = document.getElementsByClassName('togglePosition')[0]
    var toggleSVG = document.getElementsByClassName('toggleSVG')[0]
    toggleBtn.classList.toggle('ativado')
    togglePosition.classList.toggle('ativo')
    toggleSVG.classList.toggle('ativo')
}