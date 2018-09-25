from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Company


class CompanyList(LoginRequiredMixin, ListView):
    model = Company
    

class CompanyDetail(LoginRequiredMixin, DetailView):
    model = Company

    
class CompanyCreate(LoginRequiredMixin, CreateView):
    model = Company
    fields = '__all__'
