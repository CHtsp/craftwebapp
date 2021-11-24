from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
config = {
    'apiKey': "AIzaSyDUFgVOBI1mGpoESnvcq6qIE8z2BzSijVE",
    'authDomain': "fir-app-68c4f.firebaseapp.com",
    'databaseURL': "https://fir-app-68c4f.firebaseio.com",
    'projectId': "fir-app-68c4f",
    'storageBucket': "fir-app-68c4f.appspot.com",
    'messagingSenderId': "239247887438",
    'appId': "1:239247887438:web:1ee3d672ee6f8cc466871f"
}
 
# Create your views here.
def home(request):
    return render(request, 'home.html')

def courses(request):
    context = {"courses_page": "active"} 
    return render(request, 'courses.html', context)

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def error(request):
    return render(request, 'error.html')

def programme(request):
    return render(request, 'programme.html')

def download(request):
    return render(request, 'download.html')

def links(request):
    context = {"links_page": "active"} 
    return render(request, 'links.html', context)

def comingsoon(request):
    context = {"comingsoon_page": "active"} 
    return render(request, 'comingsoon.html', context)

def register(request):
    return render(request, "register.html")

def dashboard(request):
    context = {"dashboard_page": "active"} 
    return render(request, "dashboard.html", context)