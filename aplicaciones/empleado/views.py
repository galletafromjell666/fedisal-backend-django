from django.shortcuts import render
from .models import Cargo, Empleado
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from .forms import EmpleadoForm
# Create your views here.

class ModificarEmpleado(UpdateView):
    template_name = 'empleado/modificar-empleado.html'
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados:app:listar-empleados')

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
class CrearEmpleado(CreateView):
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