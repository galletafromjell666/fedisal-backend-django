from django.urls import path
from . import views
app_name = 'inicio_app'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/listar-personas/', views.listar_personas),
    path('inicio/listar-personas-tarea/', views.listar_personas_tarea),
    path('inicio/crypto/', views.crypto_price),
    path('inicio/users_list/', views.users_list),
]
