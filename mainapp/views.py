from django.shortcuts import render
from .models import OurMembers3, OurCustomers2

def anasayfa(request):

    return render(request, 'mainapp/anasayfa.html', {})

def hesap (request):
    return render(request, 'mainapp/hesap.html', {})

def members (request):
    pers = OurMembers3.objects.all()
    pers_say = len(pers)
    items_members3 = OurMembers3.objects.all()
    return render(request, 'mainapp/members.html', {'items_members3': items_members3,
                                                    'pers':pers,
                                                    'pers_say':pers_say})

def projects (request):
    return render(request, 'mainapp/projects.html', {})

def products (request):
    return render(request, 'mainapp/products.html', {})

def analysis (request):
    return render(request, 'mainapp/analysis.html', {})

def customers (request):
    cuss = OurCustomers2.objects.all()
    cuss_say = len(cuss)
    return render(request, 'mainapp/customers.html', {'cuss':cuss, 'cuss_say':cuss_say})

def budget (request):
    return render(request, 'mainapp/budget.html', {})
