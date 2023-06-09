from django.shortcuts import render
from django.db import connection
import json


# Create your views here.


def accueil(request):

    pays = None
    with connection.cursor() as cursor:
        # requete = "SELECT * FROM Chambre;"
        # requete2 = "SELECT *  FROM Hotel;"
        requete = "select ch.nom_chambre,ch.description,ch.prix_chambre,ch.image,hotel.nom from Chambre ch,Hotel hotel where ch.idHotel = hotel.idHotel;"
        cursor.execute(requete)
        mes_chambres = cursor.fetchall()
        # data = zip(mes_hotel,mes_chambres)
    # if request.method == 'POST':
    #     data = json.loads(request.body)     
    #     pays = data['pays_selected']
    #     print(data)

    context = {
        'chambres' : mes_chambres,
        'pays_select':pays,
    }    
    
    return render(request,'my_hotel/accueil_hotel.html',context)

def reserver(request):

    return render(request,'reservation/reservation.html')