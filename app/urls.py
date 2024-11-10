from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Webisite.views import home_view, voluntario_view



urlpatterns = [
    path('admin/', admin.site.urls),       # Admin do Django
    path('', home_view),                   # Página inicial
    path('voluntario/', voluntario_view, name='voluntario')  # Página do voluntário
]

# Se estiver em ambiente de desenvolvimento (DEBUG = True), servir arquivos estáticos e de mídia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)