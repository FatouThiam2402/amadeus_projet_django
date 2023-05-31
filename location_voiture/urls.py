from django.urls import path
from . import views

urlpatterns = [
    path('html_voiture/', views.index, name='index'),
     
]

