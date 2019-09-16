from django.db import models
from apps.estudiantes.models import ModelBase, Estudiante, Planificador
from apps.utils.print_colors import _green
from collections import namedtuple


class Horario(ModelBase):
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return str(self.hora_inicio) + " - " + str(self.hora_fin)

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'


class Curso(ModelBase):
    nombre = models.CharField(max_length=100)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estudiantes = models.ManyToManyField(Estudiante, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def estudiantes_asociados_count(self):
        return self.estudiantes.count()

    def anadir_estudiante(self, estudiante):

        def overlap_validation(start1, end1, start2, end2):
            return end1 >= start2 and end2 >= start1

        hora_inicio = self.horario.hora_inicio
        hora_fin = self.horario.hora_fin
        fecha_inicio = self.fecha_inicio
        fecha_fin = self.fecha_fin

        Range = namedtuple('Range', ['start', 'end'])
        r1 = Range(start=fecha_inicio, end=fecha_fin)
        flag = True

        planificadores = Planificador.objects.filter(estudiante=estudiante)
        for pl in planificadores:
            r2 = Range(start=pl.fecha_inicio, end=pl.fecha_fin)
            latest_start = max(r1.start, r2.start)
            earliest_end = min(r1.end, r2.end)
            delta = (earliest_end - latest_start).days + 1
            overlap = max(0, delta)
            if overlap > 0:
                if overlap_validation(hora_fin, hora_fin, pl.horario.hora_inicio, pl.horario.hora_fin):
                    flag = False
                    break
        if flag:
            horario = Horario.objects.create(
                hora_inicio=hora_inicio,
                hora_fin=hora_fin,
            )
            planificador = Planificador.objects.create(
                horario=horario,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                estudiante=estudiante
            )
            print(_green(planificador))
            self.estudiantes.add(estudiante)
            return True
        return False


