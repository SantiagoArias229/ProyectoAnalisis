from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index, name='index'),
    path('secante/', views.secante, name='secante'),
    path('biseccion/', views.biseccion, name='biseccion'),
    path('rf/', views.rf, name='rf'),
    path('pf/', views.pf, name='pf'),
    path('newton1/', views.newton1, name='newton1'),
    path('rm/', views.raices_multiples, name='rm'),
    
    #MODULE 2
    path('sor/', views.sor, name='sor'),
    path('gauss-seidel/', views.gs, name='gs'),
    path('newton-interpolante/', views.newtonint, name="newtonint"),
    
    #MODULE 3
     path('lagrangem/', views.lagrangem, name='lagrangem'),
]
