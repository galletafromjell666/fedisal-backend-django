from django import forms
from django.forms import ModelForm
from .models import Empleado
from django.core.exceptions import ValidationError
class EmpleadoForm(ModelForm):
    correo =  forms.EmailField(max_length=200)
    class Meta:
        model = Empleado
        fields = ['nombre','correo', 'sueldo', 'activo','cargo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'})
        }
    def clean_correo(self):
        email = self.cleaned_data['correo']
        ident = self.cleaned_data['nombre']
        #the exclude allows to preserve the same email 
        lista = Empleado.objects.filter(correo=email).exclude(nombre=ident)
        if lista:
            #raise ValidationError('El correo ya existe')
            self.add_error('correo', 'el correo ya esta usado')
        if not email.endswith(('gmail.com','yahoo.com')):
            self.add_error('correo','dominio no valido')
        
        return email