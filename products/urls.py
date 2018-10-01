from django.urls import path

from .views import ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete


app_name = "products"

urlpatterns = [
    path('', ProductList.as_view(), name="list"),
    path('new', ProductCreate.as_view(), name="new"),
    path('<int:pk>/', ProductDetail.as_view(), name="detail"),
    path('<int:pk>/edit', ProductUpdate.as_view(), name="edit"),
    path('<int:pk>/delete', ProductDelete.as_view(), name="confirm_delete"),
]
