from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "myshop/index.html")
    # return HttpResponse("<h1>Bienvenue dans ma boutique</h1>")
