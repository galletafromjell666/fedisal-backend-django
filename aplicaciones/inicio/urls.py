from django.urls import path
from . import views
urlpatterns = [
    path('inicio/hola/', views.inicio),
    path('inicio/listar-personas/', views.listar_personas),
    path('inicio/listar-personas-tarea/', views.listar_personas_tarea),
]
