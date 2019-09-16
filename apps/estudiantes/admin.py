from django.contrib import admin

from . import models


@admin.register(models.Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'apellido',
        'edad',
        'correo',
        'archived'
    ]
    search_fields = [
        'nombre',
        'apellido',
        'correo'
    ]

    list_filter = [
        'edad',
    ]


@admin.register(models.Planificador)
class PlanificadorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'fecha_inicio',
        'fecha_fin',
        'horario',
        'archived'
    ]
    search_fields = [
        'id',
    ]

    list_filter = [
        'fecha_inicio',
        'fecha_fin',
    ]
