        function generarMatrizA() {
            var filas = parseInt(document.getElementById("filas").value); 
            var tabla = document.getElementById("matrizInput");

            // Limpiar la tabla
            tabla.innerHTML = '';

            for (var i = 0; i < filas; i++) {
                var fila = tabla.insertRow(i);

                for (var j = 0; j < filas; j++) {
                    var celda = fila.insertCell(j);
                    var input = document.createElement("input");
                    input.type = "number";
                    input.name = "matriz[" + i + "][" + j + "]";
                    celda.appendChild(input);
                }
            }
        }

        function generarMatrizb() {
            var filas = parseInt(document.getElementById("filas").value);
            var columnas = 1
            var tabla = document.getElementById("matrizInputx0");

            // Limpiar la tabla
            tabla.innerHTML = '';

            for (var i = 0; i < filas; i++) {
                var fila = tabla.insertRow(i);

                for (var j = 0; j < columnas; j++) {
                    var celda = fila.insertCell(j);
                    var input = document.createElement("input");
                    input.type = "number";
                    input.name = "matriz[" + i + "][" + j + "]";
                    celda.appendChild(input);
                }
            }
        }


        function generarMatrizx0() {
            var filas = parseInt(document.getElementById("filas").value);
            var columnas = 1
            var tabla = document.getElementById("matrizInputB");

            // Limpiar la tabla
            tabla.innerHTML = '';

            for (var i = 0; i < filas; i++) {
                var fila = tabla.insertRow(i);

                for (var j = 0; j < columnas; j++) {
                    var celda = fila.insertCell(j);
                    var input = document.createElement("input");
                    input.type = "number";
                    input.name = "matriz[" + i + "][" + j + "]";
                    celda.appendChild(input);
                }
            }
        }


// ...

function guardarMatrices() {
    var matrizA = obtenerMatriz("matrizInput");
    var matrizB = obtenerMatriz("matrizInputB");
    var matrizX0 = obtenerMatriz("matrizInputx0");

    var tol = document.getElementById("tolerancia").value;
    var niter = document.getElementById("niter").value;

    // Obtener el token CSRF de la cookie
    var csrftoken = getCookie('csrftoken');

    // Enviar ambas matrices al servidor usando AJAX (jQuery) con el token CSRF
    $.ajax({
        url: "/module1/gauss-seidel/",  // Ajusta la URL según tu configuración
        type: "POST",
        data: {
            matrizA: JSON.stringify(matrizA),
            matrizB: JSON.stringify(matrizB),
            matrizX0: JSON.stringify(matrizX0),
            tol: tol,
            niter: niter,
        },
        headers: { "X-CSRFToken": csrftoken },
        success: function(data) {

                $('#radio').text(data.radio);

                // Llenar el encabezado de la tabla con las columnas
                var encabezado = $('#encabezado');
                $.each(data.columnas, function(index, columna) {
                    encabezado.append('<th>' + columna + '</th>');
                });

                // Llenar la tabla con los datos recibidos
                var tbody = $('#tablaDatos tbody');
                $.each(data.datos, function(index, fila) {
                    var tr = $('<tr>');
                    $.each(data.columnas, function(index, columna) {
                        tr.append('<td>' + fila[columna] + '</td>');
                    });
                    tbody.append(tr);
                });
        },
        error: function(error) {
            console.error("Error al guardar las matrices:", error);
        }
    });

    return false
}

function obtenerMatriz(tablaId) {
    var matriz = [];
    var filas = document.getElementById(tablaId).rows.length;

    for (var i = 0; i < filas; i++) {
        var fila = document.getElementById(tablaId).rows[i];
        var columnas = fila.cells.length;
        var filaMatriz = [];

        for (var j = 0; j < columnas; j++) {
            var valor = fila.cells[j].getElementsByTagName("input")[0].value;
            filaMatriz.push(valor);
        }

        matriz.push(filaMatriz);
    }

    return matriz;
}



// Función para obtener el valor del token CSRF de la cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
