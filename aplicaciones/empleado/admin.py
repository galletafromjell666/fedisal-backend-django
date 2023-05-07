from django.contrib import admin
from .models import Empleado, Cargo, Proyecto
# Register your models here.

#custom
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','correo','sueldo','cargo', 'activo')
    search_fields = ('nombre', 'correo')
    list_filter = ('cargo',)

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Cargo)
admin.site.register(Proyecto)