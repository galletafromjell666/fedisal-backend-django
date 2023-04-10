from django import forms
from django.forms import ModelForm
from .models import Empleado
class EmpleadoForm(ModelForm):
    correo =  forms.EmailField(max_length=200)
    class Meta:
        model = Empleado
        fields = ['nombre','correo', 'sueldo', 'activo','cargo']