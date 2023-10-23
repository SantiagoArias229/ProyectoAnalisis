from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
import matlab.engine
import pandas as pd
# Create your views here.

def home(request):
    return render(request, "home.html")


def reglafalsa(request):
    if request.method == "POST":
        #funcion = request.POST["funcion"]
        xi = float(request.POST["xi"])
        xs = float(request.POST["xs"])
        Tol = 0.000005
        niter = 100.0

        # Ejecutar el código de MATLAB
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


def biseccion(request):
    if request.method == "POST":
        # Ejecutar el código de MATLAB        
        # x = eng.FalsaPosicion(float(xi), float(xs), float(Tol), float(niter))
        # Obtener la tabla de MATLAB

        eng = matlab.engine.start_matlab()

        resultado = eng.Biseccion(str(request.POST["func"]) ,float(request.POST["xi"]), float(request.POST["xs"]), float(request.POST["tol"]), float(request.POST["iteraciones"]))
        
        a = matlab.double(resultado)
        
        
        biseccion_model = BiseccionModel(func = request.POST["func"], xi = request.POST["xi"], xs=request.POST["xs"], tol = request.POST["tol"], iteraciones = request.POST["iteraciones"])
        
        
        
        tabla_dict = [{'Iteration': row[0], 'a': row[1], 'xi': row[2], 'b': row[3], 'f': row[4], 'Error': row[5]} for row in a]
        
        print(tabla_dict)
        
        context = {
        'tabla': tabla_dict,
        'biseccion_model': biseccion_model,
        }
        
        biseccion_model.save()
        
        
        return render(request, "biseccion.html", context)

    else:
        return render(request, "biseccion.html")