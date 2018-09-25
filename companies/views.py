from django.views.generic import ListView
from .models import Company


class CompanyList(ListView):
    model = Company
    
