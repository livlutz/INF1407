onload = () => {
    (document.getElementById('insere') as HTMLButtonElement).addEventListener('click', evento => {
        evento.preventDefault();

        //TODO: colocar mensagem "em  andamento" em azul

        const elements = (document.getElementById('meuFormulario') as HTMLFormElement).elements as HTMLFormControlsCollection;
        let data: Record<string, string> = {}; //objeto usado para armazenar os dados do formulário
        for (let i = 0; i < elements.length; i++) {
            const element = elements[i] as HTMLInputElement;
            data[element.name] = element.value;
        }

        //enviar os dados para o backend
        fetch(backendAddress + "carros/umcarro/", {
            method: 'POST', body: JSON.stringify(data),
            headers: { 'Content-Type': 'application/json' }
        })


        .then(response => {
            //TODO: mudar a mensagem para verde
            if(response.ok) {
                (document.getElementById('mensagem') as HTMLDivElement).innerHTML = 'Dados inseridos com sucesso.';
            }
            else {
                //TODO: mudar a mensagem para vermelho
                (document.getElementById('mensagem') as HTMLDivElement).innerHTML = 'Erro ao inserir dados.';
            }
        })


        .catch(error => { console.log(error) })
    });
}