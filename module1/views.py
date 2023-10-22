from django.shortcuts import render

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

        # Guardar el resultado en la base de datos
        regla_falsa_model = ReglaFalsaModel( a=xi, b=xs, error=x[0], iteracions=x[1])
        regla_falsa_model.save()

        return HttpResponseRedirect("module1/reglafalsa")

    return render(request, "reglafalsa.html")