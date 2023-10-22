from django.urls import path
from . import views

urlpatterns = [
    path('reglaFalsa/', views.reglafalsa, name='reglafalsa'),
]
