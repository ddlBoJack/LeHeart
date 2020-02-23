"""Lexin_Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include
from django.views.generic import TemplateView
from board import views as bviews

urlpatterns = [
    path('home/', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('news/', bviews.news, name='news'),
    path('kepu/', bviews.kepu, name='kepu'),
    path('ceshi/', TemplateView.as_view(template_name='404.html'), name='ceshi'),
    path('yuyue/', TemplateView.as_view(template_name='404.html'), name='yuyue'),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('single/', TemplateView.as_view(template_name='single.html'), name='404'),
]
