from django.shortcuts import render
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