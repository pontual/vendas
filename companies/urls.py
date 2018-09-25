from django.urls import path

from .views import CompanyList


app_name = "companies"

urlpatterns = [
    path('', CompanyList.as_view(), name="list"),
]
