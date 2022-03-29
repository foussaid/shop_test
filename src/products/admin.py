from django.contrib import admin
from products.models import Product


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    # les éléments de mon produit  à afficher
    list_display = ("label", "type", "gtin", "expirationDate")

    # pour éditer cetains champs à l'intérieur de l'interface d'administration


admin.site.register(Product, ProductsAdmin)
