from django.shortcuts import render
from .models import Menu, Cake, CupCake

def menu(request):
    menus= Menu.objects
    return render(request, 'menu/menu.html', {'menus':menus})


def cakes(request):
    cakes= Cake.objects
    return render(request, 'menu/cakes.html', {'cakes':cakes})


def cupcakes(request):
    cupcakes= CupCake.objects
    return render(request, 'menu/cupcakes.html', {'cupcakes':cupcakes})


def cookies(request):
    return render(request, 'menu/cookies.html')


def treats(request):
    return render(request, 'menu/treats.html')

    
