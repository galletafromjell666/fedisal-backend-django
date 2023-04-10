from django.urls import path
from . import views

app_name = 'empleados_app'

urlpatterns = [
    path('empleado/crear-empleado/',
         views.CrearEmpleado.as_view(), name='crear-empleado'),
           path('empleado/crear-empleado2/',
         views.CrearEmpleado2.as_view(), name='crear-empleado2')
]
