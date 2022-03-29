from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Product(models.Model):
    label = models.CharField(max_length=100) #marque du produit
    type = models.CharField(max_length=100) #nature du produit
    gtin = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(blank=True, null=True)
    expirationDate = models.DateField()


    def get_absolute_url(self):
        #se rediriger vers l'accueil du blog quand on crée un article
        return reverse('products:home')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.gtin)
        super().save(*args, **kwargs)
