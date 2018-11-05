from django.db import models

from products.models import Product
from companies.models import Company


def sobram(self):
    all_chegandos = Chegando.objects.filter(produto=self.produto)
    total_chegando = sum(a.qtde for a in all_chegandos)
    
    aguardandos = Aguardando.objects.filter(produto=self.produto, estado__nome="Container")
    total_aguardando = sum(a.qtde - a.ja_separado for a in aguardandos)

    return total_chegando - total_aguardando
        

class Estado(models.Model):

    ordem = models.IntegerField()
    nome = models.CharField(max_length=80)


    class Meta:
        ordering = ['ordem']

        
    def __str__(self):
        return "{}".format(self.nome.upper())


class Aguardando(models.Model):

    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    qtde = models.IntegerField()
    ja_separado = models.IntegerField(default=0)
    cliente = models.ForeignKey(Company, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    container = models.CharField(max_length=20, blank=True)
    
    obs = models.CharField(max_length=200, blank=True)
    data_hora = models.DateTimeField(auto_now_add=True)

    sobram = sobram  # for use in template
    
    class Meta:
        ordering = ['estado', 'container', 'produto', 'data_hora']

        
    def __str__(self):
        return "{} qtde:{} sep:{} {} {} <{}> {}".format(
            self.produto.code,
            self.qtde,
            self.ja_separado,
            ' '.join(self.cliente.business_name.split()[:3]).title(),
            self.estado,
            self.container,
            self.data_hora)
        
        
class Chegando(models.Model):

    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    qtde = models.IntegerField()
    container = models.CharField(max_length=20)

    sobram = sobram  # for use in template

    class Meta:
        ordering = ['container', 'produto']

        
    def __str__(self):
        return "{} {} {}".format(self.produto.code, self.qtde, self.container)
