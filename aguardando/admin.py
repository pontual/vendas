from django.contrib import admin

from .models import Estado, Aguardando, Chegando


admin.site.register(Estado)
admin.site.register(Aguardando)
admin.site.register(Chegando)
