from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from apps.cursos import models, serializers
from apps.estudiantes import serializers as est_serializers
from apps.utils.shortcuts import get_object_or_none


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = models.Estudiante.objects.all()
    serializer_class = est_serializers.EstudianteSerializer

    @action(detail=True, methods=['get'])
    def cursos_asociados(self, request, pk=None):
        estudiante = get_object_or_none(models.Estudiante, id=pk)
        if estudiante:
            serializer = serializers.CursoEstudianteSerializer(estudiante.cursos_asociados_list(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'status': 'not found'}, status=status.HTTP_404_NOT_FOUND)