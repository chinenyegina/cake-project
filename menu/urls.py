from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu, name='menu'),
    path('cakes/', views.cakes, name='cakes'),
    path('cupcakes/', views.cupcakes, name='cupcakes'),
    path('cookies/', views.cookies, name='cookies'),
    path('treats/', views.treats, name='treats'),
]
