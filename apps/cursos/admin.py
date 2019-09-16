from django.contrib import admin

from django.contrib import admin

from . import models


@admin.register(models.Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'hora_inicio',
        'hora_fin',
        'archived'
    ]
    search_fields = [
        'hora_inicio',
        'hora_fin',
    ]


@admin.register(models.Curso)
class CursoAdmin(admin.ModelAdmin):
    filter_horizontal = ('estudiantes',)
    list_display = [
        'id',
        'nombre',
        'horario',
        'fecha_inicio',
        'fecha_fin',
        'archived'
    ]
    search_fields = [
        'id',
        'nombre',
    ]

    list_filter = [
        'fecha_inicio',
        'fecha_fin'
    ]