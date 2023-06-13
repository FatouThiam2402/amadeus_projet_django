from django.shortcuts import render
from django.db import connection
import json
from django.core.paginator import Paginator

from django.views.generic import ListView


# Create your views here.


class accueil(ListView):

    pays = None
    with connection.cursor() as cursor:
        # requete = "SELECT * FROM Chambre;"
        # requete2 = "SELECT *  FROM Hotel;"
        requete = "select ch.nom_chambre,ch.description,ch.prix_chambre,ch.image,hotel.nom from Chambre ch,Hotel hotel where ch.idHotel = hotel.idHotel;"
        cursor.execute(requete)
        queryset = cursor.fetchall()
        paginate_by = 8  # Remplacez 10 par le nombre d'images souhaité par page
        # return render(request, 'template.html', {'page_obj': page_obj})
        template_name = 'my_hotel/accueil_hotel.html'
        

        # data = zip(mes_hotel,mes_chambres)
    # if request.method == 'POST':
    #     data = json.loads(request.body)     
    #     pays = data['pays_selected']
    #     print(data)


def reserver(request):

    return render(request,'reservation/reservation.html')