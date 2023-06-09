from django.urls import path, include
from . import views
from django.urls import path


urlpatterns = [
    path('', views.acceuil, name='acceuil'),
    path('espaceClient/', views.login, name='login'),
    path('pageClient/', views.seConnecter, name='seConnecter'),
    path('', views.logout, name='logout'),
]
