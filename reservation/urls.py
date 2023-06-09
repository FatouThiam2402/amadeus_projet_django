from django.urls import path
from . import views

urlpatterns = [
    path('paiement/<int:idvol>/<str:villedpt>/<str:datedpt>/<str:villearriv>/<str:siegedispo>/', views.paiement, name='paiement'),

]

