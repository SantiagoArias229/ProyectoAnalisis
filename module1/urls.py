from django.urls import path
from . import views

urlpatterns = [
    path('secante/', views.secante, name='secante'),
    path('biseccion/', views.biseccion, name='biseccion'),
    path('rf/', views.rf, name='rf'),
    path('pf/', views.pf, name='pf'),
    path('newton1/', views.newton1, name='newton1'),
]
