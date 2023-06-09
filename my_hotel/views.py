from django.shortcuts import render
from django.db import connection
from django.views.generic import ListView


# Create your views here.


class accueil(ListView):

        cursor = connection.cursor() 
        query = "select ch.nom_chambre,ch.description,ch.prix_chambre,ch.image,hotel.nom from Chambre ch,Hotel hotel where ch.idHotel = hotel.idHotel;"
        cursor.execute(query)
        template_name='my_hotel/accueil_hotel.html'
        queryset = cursor.fetchall()
        paginate_by = 8
        
        
        
        # data = zip(mes_hotel,mes_chambres)
    # context = {
    #     'chambres' : mes_chambres,
       
    # }    
    
    # return render(request,'my_hotel/accueil_hotel.html',context)
