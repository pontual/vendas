from django.urls import path

from .views import CompanyList, CompanyDetail, CompanyCreate, CompanyUpdate, CompanyDelete


app_name = "companies"

urlpatterns = [
    path('', CompanyList.as_view(), name="list"),
    path('new', CompanyCreate.as_view(), name="new"),
    path('<int:pk>/', CompanyDetail.as_view(), name="detail"),
    path('<int:pk>/edit', CompanyUpdate.as_view(), name="edit"),
    path('<int:pk>/delete', CompanyDelete.as_view(), name="confirm_delete"),
]
