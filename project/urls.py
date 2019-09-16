from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import base as settings
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Django api-reto API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('', schema_view),
    path('api/v1/estudiantes/', include('apps.estudiantes.urls')),
    path('api/v1/cursos/', include('apps.cursos.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

