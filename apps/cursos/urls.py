from django.urls import path, include
from rest_framework import routers
from . import viewsets

router = routers.DefaultRouter()
router.register(r'horarios', viewsets.HorarioCursoViewSet)
router.register(r'', viewsets.CursoViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]
