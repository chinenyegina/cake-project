from django.shortcuts import render
from .models import Special


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def services(request):
    specials= Special.objects
    return render(request, 'pages/services.html', {'specials': specials})
