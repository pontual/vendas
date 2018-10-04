from decimal import Decimal

from django.db import models
from django.urls import reverse

from transactions.models import Currency


class Product(models.Model):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=120, blank=True)
    active = models.BooleanField(default=True)

    photo = models.ImageField(upload_to='product_photos/', blank=True, null=True)
    
    ean = models.CharField(max_length=32, blank=True)
    quantity_per_box = models.IntegerField(default=0)
    
    ncm = models.CharField(max_length=32, blank=True, verbose_name="NCM")
    ii = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.0'), verbose_name="I.I.")
    cest = models.CharField(max_length=20, blank=True, verbose_name="CEST")
    icms = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.0'), verbose_name="ICMS")
    ipi = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.0'), verbose_name="IPI")

    weight = models.IntegerField(default=0)

    default_sale_currency = models.ForeignKey(Currency, blank=True, null=True, on_delete=models.SET_NULL)
    default_sale_price = models.DecimalField(max_digits=12, decimal_places=4, default=Decimal('0.0'))


    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'pk': self.pk})
        

    class Meta:
        ordering = ['code']

        
    def __str__(self):
        return "{} {}".format(self.code, self.name)
