from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Courses

# config = {
#     'apiKey': "AIzaSyDUFgVOBI1mGpoESnvcq6qIE8z2BzSijVE",
#     'authDomain': "fir-app-68c4f.firebaseapp.com",
#     'databaseURL': "https://fir-app-68c4f.firebaseio.com",
#     'projectId': "fir-app-68c4f",
#     'storageBucket': "fir-app-68c4f.appspot.com",
#     'messagingSenderId': "239247887438",
#     'appId': "1:239247887438:web:1ee3d672ee6f8cc466871f"
# }
# Create your views here.
def dashboard(request):
    # if not request.user.is_authenticated :
    #     return redirect('/loginForm')

    context = {'dashboard_page' : 'active'}
    return render(request, 'dashboard.html', context)

def courses(request):
    data=Courses.objects.all()
    return render(request, 'courses.html', {
        'courses_page' : 'active',
        'data': data
    })

def coursesDetail(request, id):
    course=Courses.objects.get(id=id)
    return render(request, 'courses_detail.html', {
        'courses_page' : 'active',
        'data': course
    })

def coursesForm(request):
    return render(request, 'courses_form.html', {
        'courses_page' : 'active',
    })

def coursesStore(request):
    key=request.POST.get('key')
    title=request.POST.get('title')
    name=request.POST.get('name')
    text=request.POST.get('text')
    credit=request.POST.get('credit')
    img_path=request.POST.get('img_path')
    courses=Courses.objects.create(
                key=key,
                title=title,
                name=name,
                text=text,
                credit=credit,
                img_path=img_path
            )
    courses.save()
    return redirect('/courses')

def loginForm(request):
    if  request.user.is_authenticated :
         return redirect('/dashboard')
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
    context = {'programme_page' : 'active'}
    return render(request, 'programme.html', context)

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
        return redirect('/signupForm')