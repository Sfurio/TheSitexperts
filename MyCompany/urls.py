"""
URL configuration for MyCompany project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('sites/', views.sites, name='sites'),
    path('request/', views.request, name='request'),
    path('types/', views.types, name='types'),
    path('websitecreation/', views.website, name='website'),
    path('seoinfo/', views.seo, name='seo'),
    path('hosting/', views.hosting, name='hosting'),
    path('success/', views.success, name='success'),





]
