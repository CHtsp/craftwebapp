from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
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
def dashboard(request):
    # if not request.user.is_authenticated :
    #     return redirect('/loginForm')

    context = {'dashboard_page' : 'active'}
    return render(request, 'dashboard.html', context)

def courses(request):
    context = {'courses_page' : 'active'}
    return render(request, 'courses.html', context)

def loginForm(request):
    return render(request, 'login.html')

def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')

    user=auth.authenticate(username=username,password=password)

    if user is not None :
        auth.login(request,user)
        return redirect('/dashboard')
    else :
        messages.add_message(request, messages.INFO, 'ไม่พบข้อมูลผู้ใช้งาน')
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/loginForm')

def error(request):
    return render(request, 'error.html')

def programme(request):
    return render(request, 'programme.html')

def download(request):
    context = {'download_page' : 'active'}
    return render(request, 'download.html', context)

def links(request):
    context = {'links_page' : 'active'}
    return render(request, 'links.html', context)

def comingsoon(request):
    context = {'comingsoon_page' : 'active'}
    return render(request, 'comingsoon.html', context)

def register(request):
    return render(request, "register.html")

def craft(request):
    return render(request, "craft.html")

def busreq(request):
    return render(request, "busreq.html")

def signupForm(request):
    return render(request, 'signup.html')

def signup(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    cfpassword=request.POST.get('cfpassword')
    if password == cfpassword :
        if User.objects.filter(username=username).exists():
           messages.add_message(request, messages.INFO, 'ชื่อผู้ใช้งานซ้ำ')
           messages.info(request,'ชื่อผู้ใช้งานซ้ำ')
           return redirect('/signupForm')
        else : 
            user=User.objects.create_user(
                username=username,
                password=password
            )
            user.save()
            auth.login(request,user)
            return redirect('/dashboard')
    else :
        messages.add_message(request, messages.INFO, 'password and confirm password ต้องตรงกัน')
        # messages.info(request,'password and confirm password ต้องตรงกัน')
        return redirect('/signupForm')