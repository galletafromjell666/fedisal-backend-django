from django.db import models
from django.db.models import Q,Sum,Count

class EmpleadoManager(models.Manager):
    
    def buscar_empleados(self, texto):
        #self es el modelo
        return self.filter(
            Q(nombre__icontains=texto)
            |
            Q(correo__icontains=texto)
        )
    def buscar_empleados_sueldo(self,mini, maxi):
        return self.filter(sueldo__gte=mini, sueldo__lte=maxi).order_by('-sueldo', 'nombre')

  
class ProyectoManager(models.Manager):
    def lista_proyectos(self,fecha1,fecha2):
        return self.values('proyecto_empleado','proyecto_empleado__nombre','nombre_proyecto','fecha_inicio','fecha_fin').filter(fecha_fin__range=(fecha1.fecha2)).order_by('fecha_fin')
