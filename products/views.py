from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product


class ProductList(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 50
    

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product

    
class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_action'] = "New"

        return context


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_action'] = "Edit"

        return context
        
        
class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('companies:list')
