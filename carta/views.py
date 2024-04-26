from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import activate
from django.views.generic import TemplateView
from .models import Bebida

def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            activate(language)
    return redirect(request.POST.get('next', '/'))

def Bienvenida(request):
    saraza= 'mierda que no queres traducir'
    return render(request,'inicio.html',{'traductionPlis' : saraza })
# Create your views here.

def comensal(request):
    return render(request,'seleccionComensal.html')

def menu(request):
    return render(request,'tipoMenu.html')

class ItemController(TemplateView):
    template_name="bebidas.html"
    def get_context_data(self, **kwargs):
        model = super().get_context_data(**kwargs)
        model["bebidas"] = Bebida.objects.all()
        return model
    
    #bebidas= Bebida.objects.all()
    #return render(request,'bebidas.html',{'bebidas': bebidas})

def bodega(request):
    return render(request, 'bodega.html')

def buscar (request):
    return render(request, "busqueda.html") 


def menus (request):
    return render(request, "menus.html")

def cafe (request):
    return render(request, "cafeteria.html") 


