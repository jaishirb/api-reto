from rest_framework import serializers
from . import models


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Horario
        fields = (
            'id',
            'hora_inicio',
            'hora_fin'
        )


class CursoSerializer(serializers.ModelSerializer):
    num_estudiantes_asociados = serializers.ReadOnlyField(source='numero_estudiantes_asociados')
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
            'num_estudiantes_asociados'
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
