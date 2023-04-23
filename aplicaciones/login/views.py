from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UsuarioNuevoForm, LoginForm
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.

class LoginUser(FormView):
    form_class = LoginForm
    success_url = reverse_lazy('inicio_app:inicio')
    template_name = 'login/login-html'
    
    def form_valid(self, form):
        credenciales = form.cleaned_data
        user = authenticate(user=credenciales['username'], password=credenciales['password'])
        if user is not None:
            login(self.request, user)
            return redirect(self.success_url)
        else:
            messages.add_message(self.request, messages.INFO('Error: credenciales incorrectas'))
            return redirect(reverse_lazy('login_app:login'))
def nuevo_usuario(request):
    form = UsuarioNuevoForm()
    if request.method=='POST':
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('inicio_app:inicio')
    return render(request,'login/nuevo_usuario.html', context={'form':form})
