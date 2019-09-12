from django.shortcuts import render
from blog.views import Blog


def home(request):
    blogs= Blog.objects
    return render(request, 'products/home.html', {'blogs':blogs})
