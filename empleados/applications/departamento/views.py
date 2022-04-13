from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)
from .models import Departamento

class DepartamentoView(TemplateView):
    template_name = 'departamento/departamento.html'

class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    context_object_name= 'ListaNumeros'
    queryset = ['1', '10', '20', '30']

class ListaDepartamento(ListView):
    template_name = "departamento/lista_departamento.html"
    model = Departamento
    context_object_name= 'lista'

class DepartamentoCreateView(CreateView):
    template_name = "departamento/add.html"
    model = Departamento
    fields = ['name', 'shor_name', 'is_active'] #tiene que ir exactamente a como esta en el modelo