from django.db import models

from apps.utils.print_colors import _green
from .managers import ApiModelManager


class ModelBase(models.Model):
    archived = models.BooleanField(default=False)
    objects = ApiModelManager()

    class Meta:
        abstract = True

    def set_state(self, state):
        self.archived = state
        self.save()

    def delete(self, using=None, keep_parents=False):
        self.set_state(True)


class Estudiante(ModelBase):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.correo

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def cursos_asociados_list(self):
        from apps.cursos.models import Curso
        return Curso.objects.filter(estudiantes__id=self.id)

    def cursos_asociados_serialized(self):
        from apps.cursos.models import Curso
        from apps.cursos.serializers import CursoEstudianteSerializer
        return CursoEstudianteSerializer(Curso.objects.filter(estudiantes__id=self.id), many=True).data


class Planificador(ModelBase):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    horario = models.ForeignKey(
        'cursos.Horario',
        on_delete=models.CASCADE
    )
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Planificador'
        verbose_name_plural = 'Planificadores'
