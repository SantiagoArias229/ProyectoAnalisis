from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import *
import matlab.engine
import pandas as pd
import json

from proyecto_analisis.settings import BASE_DIR
import os

# Create your views here.

def matriz_a_string(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = "["
    for i in range(filas):
        resultado += " ".join(map(str, matriz[i]))
        if i < filas - 1:
            resultado += "; "
    resultado += "]"
    return resultado

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")

def pf(request):
    if request.method == "POST":
        # Ejecutar el código de MATLAB        
        # x = eng.FalsaPosicion(float(xi), float(xs), float(Tol), float(niter))
        # Obtener la tabla de MATLAB

        eng = matlab.engine.start_matlab()

        result = eng.puntoFijo(str(request.POST["func"]), str(request.POST["funcg"]), float(request.POST["x0"]),  float(request.POST["Tol"]), float(request.POST["niter"]), float(request.POST["error"]))
        
        df = pd.read_csv('tables/tabla_puntoFijo.csv')
        df = df.astype(str)
        data = df.to_dict(orient='records')
        
        puntoFijo_model = pfModel(func = request.POST["func"], funcg = request.POST["funcg"], x0 = request.POST["x0"], Tol = request.POST["Tol"], niter = request.POST["niter"], error = request.POST["error"], resultado = result)
        
        context = {
        'puntoFijo_model': puntoFijo_model,
        'data': data,
        'settings': settings,
        }
        
        puntoFijo_model.save()

        eng.quit()
        
        return render(request, "pf.html", context)

    else:
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

        result = eng.secante(str(request.POST["func"]) ,float(request.POST["x0"]), float(request.POST["x1"]), float(request.POST["Tol"]), float(request.POST["niter"]))
        
        df = pd.read_csv('tables/tabla_secante.csv')
        df = df.astype(str)
        data = df.to_dict(orient='records')
        

        secante_model = secanteModel(func = request.POST["func"], x0 = request.POST["x0"], x1=request.POST["x1"], Tol = request.POST["Tol"], niter = request.POST["niter"],resultado=result)
        secante_model.save()
        context = {
            'secante_model': secante_model,
            'data': data,
            'settings': settings,
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
    
def sor(request):
    if request.method == "POST":
        # Ejecutar el código de MATLAB        
        # x = eng.FalsaPosicion(float(xi), float(xs), float(Tol), float(niter))
        # Obtener la tabla de MATLAB

        eng = matlab.engine.start_matlab()

        result = eng.sor(str(request.POST["func"]), str(request.POST["funcg"]), float(request.POST["x0"]),  float(request.POST["Tol"]), float(request.POST["niter"]), float(request.POST["error"]))
        
        df = pd.read_csv('tables/tabla_puntoFijo.csv')
        df = df.astype(str)
        data = df.to_dict(orient='records')
        
        puntoFijo_model = pfModel(func = request.POST["func"], funcg = request.POST["funcg"], x0 = request.POST["x0"], Tol = request.POST["Tol"], niter = request.POST["niter"], error = request.POST["error"], resultado = result)
        
        context = {
        'puntoFijo_model': puntoFijo_model,
        'data': data,
        'settings': settings,
        }
        
        puntoFijo_model.save()

        eng.quit()
        
        return render(request, "pf.html", context)

    else:
        return render(request, "pf.html")


# Metodo para gauss-seidel
@csrf_exempt
def gs(request):
    if request.method == 'POST':
        matriz_a = json.loads(request.POST.get('matrizA'))
        matriz_b = json.loads(request.POST.get('matrizB'))
        matriz_x0 = json.loads(request.POST.get('matrizX0'))
        
        tol = request.POST.get('tol')
        niter = request.POST.get('niter')
        
        gaussSeidel_model = gsModel(A=matriz_a, b=matriz_b, x0=matriz_x0,tol = tol, niter = niter)
        gaussSeidel_model.save()
        
        eng = matlab.engine.start_matlab()
        
        matA = [[float(element) for element in sublist] for sublist in matriz_a]
        matB = [[float(element) for element in sublist] for sublist in matriz_b]
        matX0 = [[float(element) for element in sublist] for sublist in matriz_x0]
        
        A = matriz_a_string(matA)
        b = matriz_a_string(matB)
        x0 = matriz_a_string(matX0)
        
        result = eng.MatGaussSeid(x0, A, b,float(tol), float(niter))
        
        print(result)
        
        
    
        return redirect(request.path_info)
    else:
        return render(request, 'Module 2/gauss-seidel.html')

@csrf_exempt   
def lineal(request):
    if(request.method=='POST'):
        
        eng = matlab.engine.start_matlab()
        
        x=request.POST.get('x')
        x=x.replace(' ','')
        
        xFile=open("puntosX.txt",'w')
        xFile.write(x)
        xFile.close()
        
        y=request.POST.get('y')
        y=y.replace(' ','')
        print(x)
        print(y)
        
        yFile=open("puntosY.txt",'w')
        yFile.write(y)
        yFile.close()

        #corremos matlab
        eng.Spline(1)
        
        try:
            csv_file = open('Spline_Lineal.csv', 'r')
            data = csv_file.readlines()
            columnNames = data[0].split(',')
            columnNames[len(columnNames)-1] = columnNames[len(columnNames)-1].replace('\n','')
            table = []
            for i in range(1, len(data)):
                row = data[i].split(',')
                row[len(row)-1] = row[len(row)-1].replace('\n','')
                table.append(row)
                csv_file.close()
        except PermissionError as e:
            print(f"Error de permisos: {e}")

        Data('grafica_lineal.png', 'Spline_Lineal.csv')    
        
        return render(request, 'lineal.html',context={'graph':True,'tabla':table,'title':columnNames})
    
    return render(request, "lineal.html", context={})

@csrf_exempt   
def cubico(request):
    if(request.method=='POST'):
        
        eng = matlab.engine.start_matlab()
        
        x=request.POST.get('x')
        x=x.replace(' ','')
        
        xFile=open("puntosX.txt",'w')
        xFile.write(x)
        xFile.close()
        
        y=request.POST.get('y')
        y=y.replace(' ','')
        print(x)
        print(y)
       
        yFile=open("puntosY.txt",'w')
        yFile.write(y)
        yFile.close()

        eng.Spline(3)
        
        try:
            csv_file = open('Spline_Lineal.csv', 'r')
            data = csv_file.readlines()
            columnNames = data[0].split(',')
            columnNames[len(columnNames)-1] = columnNames[len(columnNames)-1].replace('\n','')
            table = []
            for i in range(1, len(data)):
                row = data[i].split(',')
                row[len(row)-1] = row[len(row)-1].replace('\n','')
                table.append(row)
                csv_file.close()
        except PermissionError as e:
            print(f"Error de permisos: {e}")

        Data('grafica_lineal.png', 'Spline_Lineal.csv')    
        
        return render(request, 'cubico.html',context={'graph':True,'tabla':table,'title':columnNames})
    
    return render(request, "cubico.html", context={})

def Data(image_name, csv_name):
    
    file_path = os.path.join(BASE_DIR, image_name)
    destination_path = os.path.join(BASE_DIR, 'module1', 'static', 'images', image_name)
    if(os.path.isfile(destination_path)):
        os.remove(destination_path)
    os.rename(file_path, destination_path)
    
    
    file_path = os.path.join(BASE_DIR, csv_name)
    destination_path = os.path.join(BASE_DIR, 'module1', 'static', 'csv', csv_name)
    if(os.path.isfile(destination_path)):
        os.remove(destination_path)
    os.rename(file_path, destination_path)