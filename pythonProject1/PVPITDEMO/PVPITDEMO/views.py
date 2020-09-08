#this file created by - namrata
from django.http import HttpResponse
from django.shortcuts import render
"""def index(request):
    return HttpResponse("Hello")
"""
def home(request):
    return render(request,'home.html')

def dashboard(request):
    return render(request,'Dashboard.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def homeimg(request):
    return render(homeimg,'home.jfif')