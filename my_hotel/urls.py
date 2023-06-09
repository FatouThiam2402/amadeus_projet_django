from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.accueil.as_view(), name = 'choixhotel'),

]  
