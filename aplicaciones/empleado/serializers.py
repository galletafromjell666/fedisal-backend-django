from .models import Cargo, Empleado, Proyecto
from rest_framework import serializers

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('nombre','correo', 'sueldo', 'activo', 'cargo', 'proyecto')

#para que la api regrese todos los datos del proyecto y no solamente su id
#empleado cargo y proyecto

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cargo
        fields = ('__all__')

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proyecto
        fields = ('__all__')

class EmpleadoCPSerializer(serializers.ModelSerializer):
    cargo = CargoSerializer()
    proyecto = ProyectoSerializer(many = True)
    class Meta:
        model = Empleado
        fields = ('id','nombre','correo', 'sueldo', 'activo', 'cargo', 'proyecto')

class ProyectoSerializer(serializers.Serializer):
    proyecto_empleado = serializers.CharField()
    proyecto_empleado__nombre = serializers.CharField()
    nombre_proyecto = serializers.CharField()
    fecha_inicio = serializers.DateField()
    fecha_fin = serializers.DateField()