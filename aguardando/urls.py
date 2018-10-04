from django.urls import path

from .views import ChegandoList, AguardandoList, summary


app_name = "aguardando"

urlpatterns = [
    path('chegando/', ChegandoList.as_view(), name="chegando_list"),
    path('aguardando/', AguardandoList.as_view(), name="aguardando_list"),
    path('summary/', summary, name="summary"),
]
