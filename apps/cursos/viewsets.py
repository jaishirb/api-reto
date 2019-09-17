import datetime

from dateutil.relativedelta import relativedelta
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from apps.cursos import models, serializers
from apps.cursos.models import Curso
from apps.estudiantes.models import Estudiante
from apps.utils.shortcuts import get_object_or_none


class HorarioCursoViewSet(viewsets.ModelViewSet):
    queryset = models.Horario.objects.all()
    serializer_class = serializers.HorarioSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = models.Curso.objects.all()
    serializer_class = serializers.CursoSerializer

    @action(detail=True, methods=['get'])
    def estudiantes_asociados(self, request, pk=None):
        curso = get_object_or_none(models.Curso, id=pk)
        if curso:
            data = {
                'cantidad': curso.numero_estudiantes_asociados()
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({'status': 'no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def agregar_estudiante(self, request, pk=None):
        id_estudiante = request.data['id_estudiante']
        estudiante = get_object_or_none(Estudiante, id=id_estudiante)
        curso = get_object_or_none(Curso, id=pk)
        if curso and estudiante:
            flag = curso.anadir_estudiante(estudiante)
            if flag:
                return Response({'status': 'exito'}, status=status.HTTP_200_OK)
            return Response({'status': 'error en registro de curso a estudiante, cruce de horario.'},
                            status=status.HTTP_406_NOT_ACCEPTABLE
                            )
        return Response({'status': 'no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def consulta_top(self, request, pk=None):
        date = datetime.datetime.now()
        init = date - relativedelta(months=6)
        cursos = list(Curso.objects.filter(fecha_inicio__gte=init))

        def custom_sort(cursos):
            return cursos.numero_estudiantes_asociados()

        cursos.sort(key=custom_sort, reverse=True)
        top = cursos[:3]
        data = {
            '1': serializers.CursoSerializer(top[0]).data,
            '2': serializers.CursoSerializer(top[1]).data,
            '3': serializers.CursoSerializer(top[2]).data,
        }
        return Response(data, status=status.HTTP_200_OK)
