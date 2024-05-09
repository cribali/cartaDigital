from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import activate
from django.views.generic import TemplateView
from .models import Item, Categoria

def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            activate(language)
    return redirect(request.POST.get('next', '/'))


def comensal(request):
    return render(request,'seleccionComensal.html')

def menu(request):
    return render(request,'tipoMenu.html')

class BebidaView(TemplateView):
    template_name="bebidas.html"
    def get_context_data(self, **kwargs):
        model = super().get_context_data(**kwargs)
        model["bebidas"] = Item.objects.filter(categoria__nombre = "bebida")
        return model
    
    #bebidas= Bebida.objects.all()
    #return render(request,'bebidas.html',{'bebidas': bebidas})

class BodegaView(TemplateView):
    template_name="bodega.html"
    def get_context_data(self, **kwargs):
        model = super().get_context_data(**kwargs)
        model["bodega"] = Item.objects.filter(categoria__nombre = "bodega")
        return model

def bodega(request):
    return render(request, 'bodega.html')

def buscar (request):
    return render(request, "busqueda.html") 


def menus (request):
    return render(request, "menus.html")

def cafe (request):
    return render(request, "cafeteria.html") 


