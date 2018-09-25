from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=64)


    class Meta:
        verbose_name_plural = 'Currencies'
        ordering = ['code']

    
    def __str__(self):
        return self.code
