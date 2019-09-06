from django.shortcuts import render
from .models import Menu

def menu(request):
    menus= Menu.objects
    return render(request, 'menu/menu.html', {'menus':menus})
