from rest_framework import serializers

from apps.estudiantes.serializers import EstudianteSerializer
from . import models
from apps.utils.shortcuts import get_object_or_none


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Horario
        fields = (
            'id',
            'hora_inicio',
            'hora_fin'
        )


class CursoSerializer(serializers.ModelSerializer):
    numero_estudiantes_asociados = serializers.ReadOnlyField(source='estudiantes_asociados_count')
    hora_inicio_read = serializers.ReadOnlyField(source='horario.hora_inicio')
    hora_fin_read = serializers.ReadOnlyField(source='horario.hora_fin')

    class Meta:
        model = models.Curso
        fields = (
            'id',
            'nombre',
            'hora_inicio_read',
            'hora_fin_read',
            'fecha_inicio',
            'fecha_fin',
            'numero_estudiantes_asociados'
        )


class CursoEstudianteSerializer(serializers.ModelSerializer):
    hora_inicio_read = serializers.ReadOnlyField(source='horario.hora_inicio')
    hora_fin_read = serializers.ReadOnlyField(source='horario.hora_fin')

    class Meta:
        model = models.Curso
        fields = (
            'id',
            'nombre',
            'hora_inicio_read',
            'hora_fin_read',
            'fecha_inicio',
            'fecha_fin',
        )
