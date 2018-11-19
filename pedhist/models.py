from django.db import models

from products.models import Product
from companies.models import Company


class Pedido(models.Model):
    created = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Company, on_delete=models.CASCADE)
    cond = models.CharField(max_length=80)
    desc = models.CharField(max_length=4)
    produtos = models.TextField()
    obs1 = models.CharField(max_length=80, blank=True)
    obs2 = models.TextField(blank=True)

    def __str__(self):
        return "{} {} {}".format(self.created, self.cliente.business_name, self.produtos)
