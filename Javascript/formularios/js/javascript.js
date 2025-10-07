onload = function() {
    let objNome = document.getElementById("nome");
    objNome.addEventListener("keyup", function() {
        console.log("O valor do campo nome foi alterado para: " + objNome.value);
    });

    //Valor do campo senha
    (objSenha=this.document.getElementById("senha")).addEventListener("blur", function() {
        console.log("O valor do campo senha foi alterado para: " + this.value);
    });

    //Evento do botão somar
    this.document.getElementById("btnSomar").addEventListener("click", function() {
        console.log("O tipo do campo num1 é: " + typeof(document.getElementById("num1").value));
        let num1 = parseFloat(document.getElementById("num1").value) || 0;
        let num2 = parseFloat(document.getElementById("num2").value) || 0;
        let resultado = num1 + num2;
        document.getElementById("resultado").value = resultado;
    });

    //Valores dos campos checkbox
    this.document.getElementById("btnVerificar").addEventListener("click", function() {
        let check1 = document.getElementById("check1").checked;
        let check2 = document.getElementById("check2").checked;
        console.log("O valor do campo check1 é: " + check1);
        console.log("O valor do campo check2 é: " + check2);
    });

    //Valores do campo radio
    this.document.getElementById("btnVerificarRadio").addEventListener("click", function() {
        let radios = document.getElementsByName("grupo1");
        let valorSelecionado = null;
        for (let i = 0; i < radios.length; i++) {
            if (radios[i].checked) {
                valorSelecionado = radios[i].value;
                break;
            }
        }
        console.log("O valor selecionado no grupo1 é: " + valorSelecionado);
    });
};
