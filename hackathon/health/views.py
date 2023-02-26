from django.shortcuts import render
from django.http import HttpResponse

from . import backend

# Create your views here.

l=backend.al()


def home_page(request):
    return render(request, 'home.html')


def recipes_page(request, slug):
    if (request.method == "POST"):
        print(slug)
        aid=0
        if slug=='hello':
            aid=2
            r=backend.get_recipe(aid)
        elif slug=='bye':
            aid=3
            r=backend.get_recipe(aid)
        else:
            aid=backend.ids(slug)
            r=backend.get_recipe(aid)
        print(aid)
        return render(request, 'recipes.html',{'rec':r})
    else:
        return render(request, 'recipes.html')  


def allergy_page(request):
    return render(request, 'allergy.html',{'list':l})

#print(l[0][1])