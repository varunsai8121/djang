from os import name
from django.urls.resolvers import URLPattern
from djang.urls import path
from . import views

urlpatterns=[
    
    path('',views.Home,name='Home'),
    path('about',views.about,name='About'),
    path('services',views.services,name='Ser'),
    path('contact',views.contact,name='Con'),
]