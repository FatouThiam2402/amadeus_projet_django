from django.urls import path
from . import views

urlpatterns = [
    path('', views.post, name="inscription"),
    path('mesreservations', views.mesreservations, name="mesreservations"),
]
