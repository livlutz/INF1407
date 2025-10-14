

var qtd = 256;

function htmlDeDentro(){
    var inicio = new Date().getTime();
    var idDiv;
    for(var i=0; i<qtd; i++){
        var campo = document.createElement("input");
        campo.setAttribute("type", "text");
        (document.getElementById("div1") as HTMLDivElement).appendChild(campo);
    }
}