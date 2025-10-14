onload = () => {
    (document.getElementById('adiciona-telefone') as HTMLButtonElement).addEventListener('click', adicionaTelefone);
    (document.getElementById('adiciona-email') as HTMLButtonElement).addEventListener('click', adicionaEmail);
}

function adicionaEmail() {
    //cria o campo de email
    var campo = "<input type='text' />";

    //cria o botão de remover o campo de email
    var botao = "<button type='button' onclick='this.parentNode.remove()'>X</button>";

    //cria a div que envolve o campo
    var div = "<div class='email'>" + campo + botao + "</div>";

    //adiciona o div na tela
    (document.getElementById("emails") as HTMLTableCellElement).innerHTML += div;
}

function adicionaTelefone() {
    //cria um campo de telefone
    var campo = document.createElement('input');
    campo.setAttribute("type", "text");

    //cria o botão de remover o campo de telefone
    var botao = document.createElement('button');
    botao.setAttribute("type", "button");
    botao.appendChild(document.createTextNode("X"));
    botao.addEventListener('click', function() {
        //remove o div que envolve o campo e o botão
        (this.parentNode as HTMLDivElement).remove();
    });

    //cria a div que envolve o campo
    var div = document.createElement('div');
    div.setAttribute("class", "telefone");
    div.appendChild(campo);
    div.appendChild(botao);

    //adiciona o div na tela
    (document.getElementById("telefones") as HTMLTableCellElement).appendChild(div);
}

