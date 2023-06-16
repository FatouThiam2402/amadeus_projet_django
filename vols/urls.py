from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='choixvol'),
    path('select_destination/<str:param>',views.select_destination, name="select_destination"),
    path('Reservation/', views.reserverVOYAGE, name="reserverVOYAGE"),
    path('monProfile/<str:param>', views.monProfile, name="monProfile"),
    # path('paiement/<int:idvol>/<str:villedpt>/<str:hdpt>/<str:harriv>/<int:siegedispo>/<str:compagnie>/<int:prix>/<str:numvol>/',
    #  views.paiement, name='paiement'),
    path('paiement/<int:idvol>/<str:villedpt>/<str:hdpt>/<str:harriv>/<int:siegedispo>/<str:compagnie>/<str:prix>/<str:numvol>/', views.paiement, name='paiement'),
    path('voldispo/', views.toutLesVols, name="toutLesVols"),
    path('voirdestination/<str:param>', views.voirdestination, name="voirdestination"),
    path('voirereservations/<str:param>', views.voirereservations, name="voirereservations"),
    path('modifierreservations/<str:param>', views.modifierreservations, name="modifierreservations"),
    path('search_offers/', views.search_offers, name="search_offers"),
    path('price_offers', views.price_offer, name="price_offer"),
    path('book_flight/', views.book_flight, name="book_flight"),
    path('GalerieVol/', views.galerie_vol.as_view(), name="galerie_vol")

]

