from rest_framework import serializers

from . import models
from apps.utils.shortcuts import get_object_or_none


class EstudianteSerializer(serializers.ModelSerializer):
    cursos_asociados = serializers.ReadOnlyField(source='cursos_asociados_serialized')

    class Meta:
        model = models.Estudiante
        fields = (
            'id',
            'nombre',
            'apellido',
            'edad',
            'correo',
            'cursos_asociados'
        )
