from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Webisite.views import home_view, voluntario_view



urlpatterns = [
    path('admin/', admin.site.urls),      
    path('', home_view),                   
    path('voluntario/', voluntario_view, name='voluntario')  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)