"use strict";
onload = () => {
    document.getElementById('insere').addEventListener('click', evento => {
        evento.preventDefault();
        //TODO: colocar mensagem "em  andamento" em azul
        const elements = document.getElementById('meuFormulario').elements;
        let data = {}; //objeto usado para armazenar os dados do formulário
        for (let i = 0; i < elements.length; i++) {
            const element = elements[i];
            data[element.name] = element.value;
        }
        //enviar os dados para o backend
        fetch(backendAddress + "carros/umcarro/", {
            method: 'POST', body: JSON.stringify(data),
            headers: { 'Content-Type': 'application/json' }
        })
            .then(response => {
            //TODO: mudar a mensagem para verde
            if (response.ok) {
                document.getElementById('mensagem').innerHTML = 'Dados inseridos com sucesso.';
            }
            else {
                //TODO: mudar a mensagem para vermelho
                document.getElementById('mensagem').innerHTML = 'Erro ao inserir dados.';
            }
        })
            .catch(error => { console.log(error); });
    });
};
