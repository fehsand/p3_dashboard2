from django.shortcuts import render
from django.contrib.auth.models import User

def anasayfa(request):
    items_members = User.objects.all()
    return render(request, 'mainapp/anasayfa.html', {'members': items_members})

def hesap (request):
    return render(request, 'mainapp/hesap.html', {})

def members (request):
    return render(request, 'mainapp/members.html', {})

def projects (request):
    return render(request, 'mainapp/projects.html', {})

def products (request):
    return render(request, 'mainapp/products.html', {})

def analysis (request):
    return render(request, 'mainapp/analysis.html', {})
