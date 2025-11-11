onload = function () {
    exibeListaDeCarros();
};
function exibeListaDeCarros() {
    console.log("Fetching from:", backendAddress + "carros/lista/");
    fetch(backendAddress + "carros/lista/")
        .then(function (response) {
        console.log("Response status:", response.status);
        console.log("Response headers:", response.headers);
        if (!response.ok) {
            throw new Error("HTTP error! status: ".concat(response.status));
        }
        return response.json();
    })
        .then(function (carros) {
        console.log("Cars received:", carros);
        var campos = ['name', 'mpg', 'cyl', 'disp', 'hp', 'wt', 'qsec', 'vs', 'am', 'gear'];
        var tbody = document.getElementById('idtbody');
        tbody.innerHTML = "";
        for (var _i = 0, carros_1 = carros; _i < carros_1.length; _i++) {
            var carro = carros_1[_i];
            var tr = document.createElement('tr');
            for (var i = 0; i < campos.length; i++) {
                var td = document.createElement('td');
                var texto = document.createTextNode(carro[campos[i]]);
                td.appendChild(texto);
                tr.appendChild(td);
            }
            tbody.appendChild(tr);
        }
        console.log("Table updated successfully");
    })["catch"](function (error) {
        console.error("Erro completo:", error);
        console.error("Erro detalhado:", error.message, error.stack);
    });
}
