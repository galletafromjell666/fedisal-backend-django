from django.urls import path
from . import views

app_name = 'empleados_app'

urlpatterns = [

    # API Views
     path('api/empleado/obtener-empleado/<pk>/',
         views.ObtenerAPIEmpleado.as_view(), name='api-obtener-empleado'),
    path('api/empleado/listar-empleados/',
         views.ListarAPIEmpleado.as_view(), name='api-listar-empleados'),
    path('api/empleado/listar-empleados2/',
         views.ListarAPIEmpleado2.as_view(), name='api-listar-empleados2'),
    path('api/empleado/crear-empleado/',
         views.CrearAPIEmpleado.as_view(), name='api-crear-empleado'),
    # Views
    path('empleado/crear-empleado/',
         views.CrearEmpleado.as_view(), name='crear-empleado'),
    path('empleado/crear-empleado2/',
         views.CrearEmpleado2.as_view(), name='crear-empleado2'),
    path('empleado/listar-empleados/',
         views.ListarEmpleados.as_view(), name='listar-empleados'),
    path('empleado/modificar-empleados/<pk>/',
         views.ModificarEmpleado.as_view(), name='modificar-empleados'),
    path('empleado/eliminar-empleados/<pk>/',
         views.EliminarEmpleado.as_view(), name='eliminar-empleados'),
]
