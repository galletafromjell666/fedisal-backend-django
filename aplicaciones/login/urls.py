from django.urls import path
from . import views
app_name = 'login_app'

urlpatterns = [
    path('login/nuevo-usuario', views.nuevo_usuario, name='nuevo-usuario'),
    path('login/', views.LoginUser.as_view(), name='login')
]
