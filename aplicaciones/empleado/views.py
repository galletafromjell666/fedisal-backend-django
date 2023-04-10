from django.shortcuts import render
from .models import Cargo, Empleado
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from .forms import EmpleadoForm
# Create your views here.

class CrearEmpleado(CreateView):
    template_name = 'empleado/crear-empleado.html'
    model = Empleado
    fields = ['nombre','correo', 'sueldo', 'activo','cargo']
    success_url = '/inicio/hola/'

class CrearEmpleado2(CreateView):
    template_name = 'empleado/crear-empleado.html'
    form_class =  EmpleadoForm
    success_url = '/inicio/hola/'