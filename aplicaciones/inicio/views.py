from django.shortcuts import render
import requests
# Create your views here.


def inicio(request):
    # we're telling to render templates/inicio/index.html, there is no need to specify
    # templates folder, since it already has been configured in config
    return render(request, 'inicio/index.html')


def listar_personas(request):
    personas = {
        'titulo': 'Lista de personas',
        'nombres': ["Maria", "Juan", "Pedro"]}
    return render(request,'inicio/listar-personas.html', personas)

def listar_personas_tarea(request):
    personas = {
        'titulo': 'Lista de personas tarea',
        'personas': [{"nombre": "Maria", "edad": 21},{"nombre": "Juan", "edad": 22},{"nombre": "Henry", "edad": 25},{"nombre": "Sara", "edad": 23},{"nombre": "Carlos", "edad": 15}]}
    return render(request,'inicio/listar-personas-tarea.html', personas)

def crypto_price(request):
    pagina = 1
    if request.GET:
        pagina = int(request.GET['page'])
    url_binance = 'https://api.binance.com/api/v3/ticker/price'
    datos = requests.get(url_binance)
    context = {'precios': datos.json()[int(pagina)*10-9:int(pagina)*10:]}
    return render(request, 'inicio/crypto_price.html', context)

def users_list(request):
    datos = requests.get('https://jsonplaceholder.typicode.com/users')
    context = {'users': datos.json()}
    return render(request, 'inicio/users_list.html', context)