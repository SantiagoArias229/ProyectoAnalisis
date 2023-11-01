from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
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

        resultado = eng.secante(str(request.POST["func"]) ,float(request.POST["x0"]), float(request.POST["x1"]), float(request.POST["Tol"]), float(request.POST["niter"],float(request.POST["error"])))
        
        a = matlab.double(resultado)
        
        
        secante_model = secanteModel(func = request.POST["func"], x0 = request.POST["x0"], x1=request.POST["x1"], Tol = request.POST["Tol"], niter = request.POST["niter"],error = request.POST["error"])

        context = {
            'secante_model': secante_model,
        }        
        
        return render(request, "secante.html", context)

    else:
        return render(request, "secante.html")



def biseccion(request):
    if request.method == "POST":
        # Ejecutar el código de MATLAB        
        # x = eng.FalsaPosicion(float(xi), float(xs), float(Tol), float(niter))
        # Obtener la tabla de MATLAB

        eng = matlab.engine.start_matlab()

        result = eng.Biseccion(str(request.POST["func"]) ,float(request.POST["xi"]), float(request.POST["xs"]), float(request.POST["tol"]), float(request.POST["iteraciones"]))
        
        
        df = pd.read_csv('tables/tabla_biseccion.csv')
        df = df.astype(str)
        data = df.to_dict(orient='records')
        
        
        biseccion_model = BiseccionModel(func = request.POST["func"], xi = request.POST["xi"], xs=request.POST["xs"], tol = request.POST["tol"], iteraciones = request.POST["iteraciones"], resultado = result)
        biseccion_model.save()
        
        context = {
        'biseccion_model': biseccion_model,
        'data': data,
        'settings': settings,
        }

        return render(request, "biseccion.html", context)

    else:
        return render(request, "biseccion.html")

def raices_multiples(request):
    if request.method == "POST":

        eng = matlab.engine.start_matlab()

        result = eng.raicesMultiples(float(request.POST["x0"]) , float(request.POST["tol"]), float(request.POST["iteraciones"]),str(request.POST["func"]))
        
        df = pd.read_csv('tables/tabla_raicesMultiples.csv')
        df = df.astype(str)
        data = df.to_dict(orient='records')
        
        rm_model = rmModel(func = request.POST["func"], x0 = request.POST["x0"], tol = request.POST["tol"], iteraciones = request.POST["iteraciones"], resultado = result)
        rm_model.save()
        
        context = {
        'rm_model': rm_model,
        'data': data,
        'settings': settings,
        }

        return render(request, "rm.html", context)

    else:
        return render(request, "rm.html")