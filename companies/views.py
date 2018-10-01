from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Company


class CompanyList(LoginRequiredMixin, ListView):
    model = Company
    paginate_by = 99
    

class CompanyDetail(LoginRequiredMixin, DetailView):
    model = Company

    
class CompanyCreate(LoginRequiredMixin, CreateView):
    model = Company
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_action'] = "New"

        return context


class CompanyUpdate(LoginRequiredMixin, UpdateView):
    model = Company
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_action'] = "Edit"

        return context
        
        
class CompanyDelete(LoginRequiredMixin, DeleteView):
    model = Company
    success_url = reverse_lazy('companies:list')
