from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from captcha.fields import CaptchaField
class UsuarioNuevoForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Clave', max_length=100, required=True, widget=forms.PasswordInput)

class CaptchaForm(forms.Form):
    captcha = CaptchaField()