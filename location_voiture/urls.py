from django.urls import path
from . import views

urlpatterns = [
    path('html_voiture/', views.index, name='index'),
    path('bouton_reservation/', views.process_reservation, name='process_reservation'),
    path('html_reservation/', views.process_recuper, name='process_recuper'),
]


