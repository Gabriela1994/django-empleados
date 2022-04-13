from django.shortcuts import render
#vistas genericas de django
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)
#import models
from .models import Prueba

from applications.home.models import Prueba

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name= 'ListaNumeros'
    queryset = ['1', '10', '20', '30']

class ListaPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name= 'lista'

class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    fields = ['titulo', 'subtitulo', 'cantidad']


