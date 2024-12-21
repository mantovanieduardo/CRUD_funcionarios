from django.shortcuts import render
from django.views.generic import (
 CreateView, ListView, UpdateView, DetailView, DeleteView
)
from django.urls import reverse_lazy
from .models import Funcionario


class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = "__all__"
    template_name = "form_funcionario.html"
    success_url = reverse_lazy('lista_funcionarios')  # Usando reverse_lazy para o nome da URL

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "lista_funcionarios.html"

class FuncionarioUpdateView(UpdateView):
 model = Funcionario
 fields = ("nome", "cpf", "email", "remuneracao")
 template_name = "form_funcionario.html"
 success_url = reverse_lazy("lista_funcionarios") 

class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = "lista_funcionario.html"
    context_object_name = "fun"  # Isso garante que você usará 'fun' no template


class FuncionarioDeleteView(DeleteView):
 model = Funcionario
 template_name = "remover_funcionario.html"
 success_url = reverse_lazy("lista_funcionarios") 