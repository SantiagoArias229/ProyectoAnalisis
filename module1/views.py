from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "home.html")

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ReglaFalsaModel

def reglafalsa(request):
    if request.method == "POST":
        #funcion = request.POST["funcion"]
        xi = float(request.POST["xi"])
        xs = float(request.POST["xs"])
        Tol = 0.000005
        niter = 100.0

        # Ejecutar el código de MATLAB
        import matlab.engine
        eng = matlab.engine.start_matlab()
        x = eng.FalsaPosicion(float(xi), float(xs), float(Tol), float(niter))
        # Obtener la tabla de MATLAB
        tabla = eng.FalsaPosicion(float(request.POST["xi"]), float(request.POST["xs"]), float(0.000005), float(100.0))

        # Serializar la tabla a JSON
        import json
        print(tabla)
        tabla_json = json.dumps(tabla)

        # Devolver la tabla serializada en la respuesta
        return HttpResponse(tabla_json, content_type="application/json")

    else:
        return render(request, "module1/reglafalsa.html")
from django.template import Library

register = Library()

@register.filter
def show_matlab_table(json_table):
    import json
    table = json.loads(json_table)

    # Generar el código HTML de la tabla
    html_table = """
    <table border="1">
        <thead>
            <tr>
                <th>Iteration</th>
                <th>xn</th>
                <th>f(xn)</th>
                <th>E</th>
            </tr>
        </thead>
        <tbody>
            {% for row in table %}
                <tr>
                    <td>{{ row[0] }}</td>
                    <td>{{ row[1] }}</td>
                    <td>{{ row[2] }}</td>
                    <td>{{ row[3] }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
    """

    # Devolver el código HTML de la tabla
    return html_table
