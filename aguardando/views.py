from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Chegando, Aguardando


class ChegandoList(LoginRequiredMixin, ListView):
    model = Chegando
    paginate_by = 25
    

class AguardandoList(LoginRequiredMixin, ListView):
    model = Aguardando
    paginate_by = 25


def summary(request):
    pass
    
