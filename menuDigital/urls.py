from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from carta.views import BebidaView, BodegaView, CafeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comensal/', views.comensal),
    path('tipo/', views.menu),
    path('set-language/', views.set_language, name='set_language'),
    path('bebidas/', BebidaView.as_view()),
    path('bodega/', BodegaView.as_view()),
    path('busqueda/', views.buscar),
    path('menus/', views.menus),
    path('cafeteria/', CafeView.as_view()),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
