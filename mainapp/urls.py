from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('hesap/', views.hesap, name='hesap'),
    path('members/', views.members, name='members'),
    path('customers/', views.customers, name='customers'),
    path('projects/', views.projects, name='projects'),
    path('products/', views.products, name='products'),
    path('analysis/', views.analysis, name='analysis'),
    path('budget/', views.budget, name='budget'),
]
