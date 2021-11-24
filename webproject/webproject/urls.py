"""webproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp import views
from webapp import templates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', views.courses),
    path('login/', views.login),
    path('signup/', views.signup),
    path('404error/', views.error),
    path('programme/', views.programme),
    path('download/', views.download),
    path('links/', views.links),
    path('comingsoon/', views.comingsoon),
    path('register/', views.register),
    path('dashboard/', views.dashboard),
    path('craft/', views.craft),
    path('busreq/', views.busreq),
]