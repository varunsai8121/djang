from multiprocessing import context
import re
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home(request):
    #context is set of variabels
    context={
        'variable':"this is sent"

    }
    return render(request,"index.html",context)
    #return HttpResponse("This is home page")
def about(request):
    return render(request,"about.html")
    #return HttpResponse("this is about")
def contact(request):
    return render(request,"contact.html")
    #return HttpResponse("hello kiddo")
def services(request):
    return render(request,"services.html")
    #return HttpResponse("hi")    
def action(request):
    return render(request,"services.html")    