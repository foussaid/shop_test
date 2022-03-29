from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from products.models import Product


# Create your views here.

def index(request):
    return render(request, "products/index.html")


# Création de la vue de l'accueil

class ShopHome(ListView):  # ListView me permet de récupérer toutes les entrées de ma BDD
    model = Product
    context_object_name = "products"  # spécifier le nom "products" pour la variable qie je vais utiliser dans les templates


# Vue pour ajouter un article
class CreateProduct(CreateView):
    model = Product
    template_name = "products/product_create.html"
    fields = ['label', 'type', 'gtin', 'expirationDate']


class ProductUpdate(UpdateView):
    model = Product
    template_name = "products/products_edit.html"
    fields = ['expirationDate']


class ProductDetail(DetailView):
    model = Product
    context_object_name = "product"


class DeleteProduct(DeleteView):
    model = Product
    # l'url verslaquelle on souhaite se rediriger une fois qu'on a supprimé un article
    success_url = reverse_lazy("products:home")
