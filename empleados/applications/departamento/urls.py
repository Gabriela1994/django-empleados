from django.urls import path
from . import views

urlpatterns = [
    path('departamento/', views.DepartamentoView.as_view()),
    path('lista/', views.DepartamentoListView.as_view()),
    path('lista_departamento/', views.ListaDepartamento.as_view()),
    path('add/', views.DepartamentoCreateView.as_view()),
]

