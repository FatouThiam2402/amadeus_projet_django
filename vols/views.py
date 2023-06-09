from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone
from django.core.paginator import Paginator
import mysql.connector
from django.views.generic import ListView
from django.contrib import messages
from django.db import connection


# Établir une connexion à la base de données
connection = mysql.connector.connect(
        host='localhost',
        user='Moussa',
        password='root123',
        database='amadeus'
)

from amadeus import Client, ResponseError, Location
amadeus = Client(
    client_id='CoArtPgeKZ5667oYQFCkFCBsv5PeV43Q',
    client_secret='PbkxxwJuP5xL5aqX'
)



def index(request) :
 	return render(request, 'vols/choixvol.html')
 	
 	

def toutLesVols(request):

    cursor = connection.cursor()
    # adults = request.POST.get('adults')
    origin = request.POST.get('origin')
    destination = request.POST.get('destination')
    # departureDate = request.POST.get('departureDate')
    # returnDate = request.POST.get('returnDate')
    # if not adults:
    #     adults = 1
    if request.method == "POST" :
        if origin != '' or destination != '':
            query = "SELECT * FROM Vol WHERE  AeroportDepart LIKE %s AND AeroportArrivee LIKE %s "
            parameters = ('%' + origin + '%', '%' + destination + '%') 
         
        else :
            messages.error(request,'Aucune donnee soumise')
            return render(request, 'vols/choixvol.html')
    cursor.execute(query, parameters)
    results = cursor.fetchall()
    if(len(results)< 0):
        flightdatas = 'no info'
        context = {'results': flightdatas}
        return render(request, 'vols/voldispo.html', context) 
    paginator = Paginator(results, 10)
    page = request.GET.get('page')
    flightdatas = paginator.get_page(page)
    context = {'results': flightdatas}
    # cursor.close()
    # connection.close()
    return render(request, 'vols/voldispo.html', context)    


class galerie_vol(ListView):
    cursor = connection.cursor()
    template_name = 'vols/galerieVol.html'
    query = "SELECT DISTINCT(ville), pays, codeVille, imagedesc, latitude, longitude  FROM Localisation ORDER BY ville"
    cursor.execute(query)
    queryset = cursor.fetchall()
    # context = {'galerie': queryset}
    # cursor.close()
    # connection.close()
    paginate_by = 8
    # return render(request, template_name, context) 
    
def voirdestination(req, param):
    cursor = connection.cursor()
    if req.method == "GET":
        template_name='vols/voldispo.html'
        query = "SELECT * FROM Vol WHERE  AeroportArrivee LIKE %s"
        parameters=[param]
        print(parameters)
        cursor.execute(query, parameters)
        results = cursor.fetchall()
        print(results)
        context = {'results': results}
        return render(req, template_name, context) 
        
          
         

def reserverVol(request):
    dateres = timezone.now()
    context = {'dateres': dateres}
    return render(request, 'reservation/paiement.html', context) 
    
def select_destination(req, param):
    if req.method == "GET":
        try:
            print(param)
            response = amadeus.reference_data.locations.get(
                keyword=param, subType=Location.ANY)
            context = {
                "data": response.data
            }
            return JsonResponse(context)

        except ResponseError as error:
            print(error)
    return JsonResponse({"error": "Invalid request method"})


def search_offers(req):
    if req.method == "GET":
        try:
            originCode = req.GET["originCode"]
            destinationCode = req.GET["destinationCode"]
            departureDate = req.GET["departureDate"]
            print(originCode, destinationCode, departureDate)
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=originCode, destinationLocationCode=destinationCode, departureDate=departureDate, adults=1)
            context = {
                "data": response.data
            }
            return JsonResponse(context)

        except ResponseError as error:
            print(error)
    else:
        return JsonResponse({"error": "Invalid request method"})


@csrf_exempt
def price_offer(req):
    if req.method == "POST":
        try:
            data = json.loads(req.body)
            flight = data.get("flight")
            response = amadeus.shopping.flight_offers.pricing.post(flight)
 
            return JsonResponse(response.data)

        except ResponseError as error:
            print(error)
    else:
       return JsonResponse({"error": "Invalid request method"})

@csrf_exempt
def book_flight(req):
    if req.method == "POST":
        try: 
            data = json.loads(req.body)
            flight = data.get('flight')
            traveler = data.get('traveler')
            booking = amadeus.booking.flight_orders.post(flight, traveler)
            return JsonResponse(booking)
        except ResponseError as error:
            print(error)
    else:
       return JsonResponse({"error": "Invalid request method"})


