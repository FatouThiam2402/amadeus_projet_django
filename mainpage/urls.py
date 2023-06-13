from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.indexpage, name = 'indexpage'),
    path("login", views.seConnecter, name='seConnecter'),
    path("logout", views.seDeconnecter, name="seDeconnecter"),
    path("register", views.sInscrire, name="sInscrire"),
    path('contact', views.contact, name="contact"),
]  
