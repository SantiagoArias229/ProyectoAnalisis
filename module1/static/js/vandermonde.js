function agregarCampos() {
    var cantidadPuntos = document.getElementById('cantidadPuntos').value;
    var camposPuntos = document.getElementById('camposPuntos');

    // Limpiamos los campos existentes
    camposPuntos.innerHTML = '';

    // Agregamos nuevos campos según la cantidad seleccionada
    for (var i = 0; i < cantidadPuntos; i++) {
        var labelX = document.createElement('label');
        labelX.textContent = 'Punto ' + (i + 1) + ':';

        var inputX = document.createElement('input');
        inputX.type = 'number';
        inputX.name = 'coordenadaX_' + i;  // Cambiamos a un formato que prefieras

        var labelY = document.createElement('label');
        labelY.textContent = 'Punto ' + (i + 1) + ':';

        var inputY = document.createElement('input');
        inputY.type = 'number';
        inputY.name = 'coordenadaY_' + i;  // Cambiamos a un formato que prefieras

        camposPuntos.appendChild(labelX);
        camposPuntos.appendChild(inputX);
        camposPuntos.appendChild(labelY);
        camposPuntos.appendChild(inputY);
        camposPuntos.appendChild(document.createElement('br'));
    }
}
