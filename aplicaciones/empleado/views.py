from django.shortcuts import render
from .models import Cargo, Empleado
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from .forms import EmpleadoForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from rest_framework.generics import (ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView,RetrieveUpdateAPIView)
from .serializers import EmpleadoSerializer, EmpleadoCPSerializer
# Create your views here.

#API Views
class ListarAPIEmpleado(ListAPIView):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()

#ListarEmpleado con serializer para expandir los campos
class ListarAPIEmpleado2(ListAPIView):
    serializer_class = EmpleadoCPSerializer
    queryset = Empleado.objects.all()

class ObtenerAPIEmpleado(RetrieveAPIView):
    serializer_class =  EmpleadoCPSerializer
    queryset = Empleado.objects.all()
class CrearAPIEmpleado(CreateAPIView):
    serializer_class =  EmpleadoSerializer
    

#Views
@method_decorator(login_required,name='dispatch')
class ModificarEmpleado(PermissionRequiredMixin,UpdateView):
    permission_required = ('empleado.change_empleado',)
    template_name = 'empleado/modificar-empleado.html'
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados:app:listar-empleados')

#using auth with decorator
@method_decorator(login_required,name='dispatch')
class ListarEmpleados(ListView):
    template_name = 'empleado/listar-empleados.html'
    model = Empleado
    context_object_name = 'lista_empleados'
    #queryset = Empleado.objects.filter(activo=True)
    paginate_by = 2

    def get_queryset(self):
        #buscar hace referencia al input text de la lista de empleados
        buscar = self.request.GET.get('buscar')
        lista = Empleado.objects.all()
        if buscar:
            lista = Empleado.objects.filter(nombre__icontains=buscar)
        return lista
    

#using auth with inheritance
class CrearEmpleado(LoginRequiredMixin,CreateView):
    template_name = 'empleado/crear-empleado.html'
    model = Empleado
    fields = ['nombre','correo', 'sueldo', 'activo','cargo']
    success_url = reverse_lazy('empleados_app:listar-empleados')

class CrearEmpleado2(CreateView):
    template_name = 'empleado/crear-empleado.html'
    form_class =  EmpleadoForm
    success_url = reverse_lazy('empleados_app:listar-empleados')

class EliminarEmpleado(DeleteView):
    template_name = 'empleado/eliminar-empleado.html'
    model =  Empleado
    success_url = reverse_lazy('empleados_app:listar-empleados')