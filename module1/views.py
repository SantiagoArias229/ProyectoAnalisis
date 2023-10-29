from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
import matlab.engine
import pandas as pd
# Create your views here.

def home(request):
    return render(request, "home.html")

def pf(request):
    return render(request, "pf.html")

def rf(request):
    return render(request, "rf.html")

def newton1(request):
    return render(request, "newton1.html")

def secante(request):
    if request.method == "POST":
        # Ejecutar el código de MATLAB        
        # x = eng.FalsaPosicion(float(xi), float(xs), float(Tol), float(niter))
        # Obtener la tabla de MATLAB

        eng = matlab.engine.start_matlab()

        resultado = eng.secante(str(request.POST["func"]) ,float(request.POST["x0"]), float(request.POST["x1"]), float(request.POST["Tol"]), float(request.POST["niter"]))
        
        a = matlab.double(resultado)
        
        
        secante_model = secanteModel(func = request.POST["func"], xi = request.POST["x0"], xs=request.POST["x1"], tol = request.POST["Tol"], iteraciones = request.POST["niter"])
       
                    
        
       
        
        
        return render(request, "secante.html", context)

    else:
        return render(request, "secante.html")



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