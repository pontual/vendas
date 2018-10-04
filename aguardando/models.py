from django.db import models

from products.models import Product
from companies.models import Company



class Estado(models.Model):

    ordem = models.IntegerField()
    nome = models.CharField(max_length=80)


    class Meta:
        ordering = ['ordem']

        
    def __str__(self):
        return "{}: {}".format(self.ordem, self.nome)


class Aguardando(models.Model):

    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    qtde = models.IntegerField()
    ja_separado = models.IntegerField(default=0)
    cliente = models.ForeignKey(Company, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    obs = models.CharField(max_length=200, blank=True)
    data = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['estado', 'data', 'cliente']

        
    def __str__(self):
        return "{} qtde:{} sep:{} {} {} {}".format(
            self.produto.code,
            self.qtde,
            self.ja_separado,
            ' '.join(self.cliente.business_name.split()[:3]).title(),
            self.estado,
            self.data)


class Chegando(models.Model):

    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    qtde = models.IntegerField()
    container = models.CharField(max_length=20)


    class Meta:
        ordering = ['container', 'produto']

        
    def __str__(self):
        return "{} {} {}".format(self.produto.code, self.qtde, self.container)
