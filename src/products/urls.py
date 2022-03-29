from django.urls import path

from .views import index, ShopHome, CreateProduct, ProductUpdate, DeleteProduct, ProductDetail

app_name = "products"

urlpatterns = [
    #path('', index, name="products-home")
    path('', ShopHome.as_view(), name="home"),
    path('create/', CreateProduct.as_view(), name="new-product"),
    path('<str:slug>/', ProductDetail.as_view(), name="show-product"),
    path('edit/<str:slug>', ProductUpdate.as_view(), name="edit-product"),
    path('delete/<str:slug>', DeleteProduct.as_view(), name="delete-product")

]