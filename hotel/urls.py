from django.urls import path
from . import views



urlpatterns = [
    path('', views.HomeView, name='index'),
    path('contact/', views.ContactView.as_view(), name="contact")
]

