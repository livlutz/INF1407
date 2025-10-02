onload = inicializa; /* atribuindo a referência da função */

contador = 0;

function inicializa(){
    console.log("Estamanos na inicializa");
    var objH1 = document.getElementById('id_titulo');
    objH1.addEventListener("mouseover", mouseNoH1);

    /* ou contador = 0; que representa o estado do objeto h1 aqui ,
    se usar var ou let vai ser variável local e não vai funcionar*/
}

/**
 * Trata o evento no título
 *
 * @param {*} evento objeto referente ao evento que aconteceu
 */
function mouseNoH1(evento){
    contador += 1;
    console.log("Mouse", contador, " vez(es) em cima do título");
}