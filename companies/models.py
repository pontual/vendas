from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Company(models.Model):
    code = models.CharField(max_length=32, blank=True)
    business_name = models.CharField(max_length=150)
    dba = models.CharField(max_length=120, blank=True)
    active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    salesperson = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    address_1 = models.CharField(max_length=120, blank=True)
    address_2 = models.CharField(max_length=120, blank=True)
    address_3 = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=80, blank=True)
    zip_code = models.CharField(max_length=18, blank=True)
    country = models.CharField(max_length=80, blank=True)
    
    contact = models.CharField(max_length=80, blank=True)

    phone_main = models.CharField(max_length=32, blank=True)
    phone_2 = models.CharField(max_length=32, blank=True)
    phone_3 = models.CharField(max_length=32, blank=True)

    email_main = models.EmailField(max_length=255, blank=True)
    email_finance = models.EmailField(max_length=255, blank=True)

    federal_id = models.CharField(max_length=32, blank=True)
    state_id = models.CharField(max_length=32, blank=True)
    city_id = models.CharField(max_length=32, blank=True)
    
    shipper = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)

    shipping_address_1 = models.CharField(max_length=120, blank=True)
    shipping_address_2 = models.CharField(max_length=120, blank=True)
    shipping_address_3 = models.CharField(max_length=120, blank=True)
    shipping_city = models.CharField(max_length=100, blank=True)
    shipping_state = models.CharField(max_length=80, blank=True)
    shipping_zip_code = models.CharField(max_length=18, blank=True)
    shipping_country = models.CharField(max_length=80, blank=True)

    notes = models.TextField(blank=True)


    def get_absolute_url(self):
        return reverse('companies:detail', kwargs={'pk': self.pk})

        
    class Meta:
        verbose_name_plural = "Companies"


    def __str__(self):
        return "[{}] {} ({})".format(self.code, self.business_name, self.salesperson)
