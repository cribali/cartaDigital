from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('comensal/', views.comensal),
    path('tipo/', views.menu),
    path('set-language/', views.set_language, name='set_language'),
    path('bebidas/', views.bebida),
    path('bodega/', views.bodega),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
