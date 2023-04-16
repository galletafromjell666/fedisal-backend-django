from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import UsuarioNuevoForm
# Create your views here.

def nuevo_usuario(request):
    form = UsuarioNuevoForm()
    return render(request,'login/nuevo_usuario.html', context={'form':form})
