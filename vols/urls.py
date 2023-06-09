from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='choixvol'),
    path('select_destination/<str:param>',views.select_destination, name="select_destination"),
    path('voldispo/', views.toutLesVols, name="toutLesVols"),
    path('voirdestination/<str:param>', views.voirdestination, name="voirdestination"),
    path('search_offers/', views.search_offers, name="search_offers"),
    path('price_offers', views.price_offer, name="price_offer"),
    path('book_flight/', views.book_flight, name="book_flight"),
    path('GalerieVol/', views.galerie_vol.as_view(), name="galerie_vol")

]

