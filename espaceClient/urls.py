from django.urls import path, include
from . import views

urlpatterns = [
    path('espaceClient/', views.login, name='login'),

]
