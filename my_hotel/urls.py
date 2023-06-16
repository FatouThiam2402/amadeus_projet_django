from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "my_hotel"

urlpatterns = [
    
    path('',views.accueil.as_view(), name = 'accueil'),
    path('reservation/',views.reserver, name = 'reserver'),

]  
