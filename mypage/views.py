from django.http import HttpResponse
from django.shortcuts import render 

# Create your views here.

def nav(request):
    return render (request,"nav.html",{})

def home(request):
    return render (request,"home.html",{})

def projects(request):
    return render (request,"projects.html",{})

def contact(request):
    name = request.POST.get('Name')
    return render (request,"contact.html",{'Name' : name})

