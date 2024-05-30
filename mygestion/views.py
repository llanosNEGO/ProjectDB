from django.shortcuts import render
from django.http import HttpResponse


# Create your models here.

def hello (request):
    return HttpResponse("<h1>Primera fase</h1>")

def segunda (request):
    return HttpResponse("<h1>Segunda fase</h1>")

def index(request):   
    return render(request,'index.html')





