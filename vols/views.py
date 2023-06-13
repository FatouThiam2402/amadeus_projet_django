from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import Paginator
import mysql.connector as sql
from datetime import datetime
from django.views.generic import ListView
from django.contrib import messages
from django.db import connection
from amadeus import Client, ResponseError, Location
from django.contrib.auth import authenticate, login, logout


# Établir une connexion à la base de données
connection = sql.connect(
        host='localhost',
        user='Moussa',
        password='root123',
        database='amadeus'
)


amadeus = Client(
    client_id='CoArtPgeKZ5667oYQFCkFCBsv5PeV43Q',
    client_secret='PbkxxwJuP5xL5aqX'
)



def index(request) :
    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        depart_date = request.POST.get('departureDate')
        seat = request.POST.get('SeatClass')
        trip_type = request.POST.get('TripType')
        if(trip_type == '1'):
            return render(request, 'vols/choixvol.html', {
            'origin': origin,
            'destination': destination,
            'depart_date': depart_date,
            'seat': seat.lower(),
            'trip_type': trip_type
        })
        elif(trip_type == '2'):
            return_date = request.POST.get('returnDate')
            return render(request, 'vols/choixvol.html', {
            'origin': origin,
            'destination': destination,
            'depart_date': depart_date,
            'seat': seat.lower(),
            'trip_type': trip_type,
            'return_date': return_date
        })
    else:
        return render(request, 'vols/choixvol.html')
 	
 


# def seConnecter(request):
#     if request.method == "POST":
#         username = request.POST["User_Email"]
#         password = request.POST["User_Password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse("index"))
            
#         else:
#             return render(request, 'vols/login.html', {
#                 "errors": "Nom d utilisateur et/ou mot de passe incorrect(s)."
#             })
#     else:
#         if request.user.is_authenticated:
#             return HttpResponseRedirect(reverse('index'))
#         else:
#             return render(request, 'vols/login.html')
 	

def toutLesVols(request):
    template_name='vols/voldispo.html'
    cursor = connection.cursor()
    # adults = request.POST.get('adults')
    origin = request.POST.get('origin')
    destination = request.POST.get('destination')
    departureDate = request.POST.get('departureDate')
    
    # depart_date = datetime.strptime(returndate, "%Y-%m-%d")
    trip_type = request.POST.get('TripType')
    classe = request.POST.get('cabin')
    if request.method == "POST" :
        if origin != '' or destination != '':
            query = "SELECT * FROM Vol WHERE  origin LIKE %s AND destination LIKE %s "
            parameters = ('%' + origin + '%', '%' + destination + '%') 
         
        else :
            messages.error(request,'Aucune donnee soumise')
            return render(request, 'vols/choixvol.html')
    cursor.execute(query, parameters)
    results = cursor.fetchall()
    print(results)
    # |time:"H:i:s"
    # row = cursor.fetchone()
    # while row is not None:
    #     compagnie = row[9]
    #     column2_value = row[1]
    if(len(results)< 0):
        flightdatas = 'no info'
        context = {'results': flightdatas}
        return render(request, 'vols/voldispo.html', context) 
    context = {'results': results, 'origin': origin, 'destination':destination, 'depart':departureDate, 'classe':classe}
    # cursor.close()
    # connection.close()
    return render(request, template_name, context)    

def paiement(request, idvol, villedpt, hdpt, harriv, siegedispo, compagnie, prix, numvol) :
        if request.user.is_authenticated:
                context = {'idvol': idvol, 'villedpt':villedpt, 'hdpt' : hdpt, 
                           'harriv': harriv, 'siegedispo':siegedispo,
                           'compagnie': compagnie, 'prix': prix, 'numvol': numvol}
                return render(request, 'vols/paiement.html', context)
        else:
                return HttpResponseRedirect(reverse("seConnecter"))
            
            
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
        query = "SELECT * FROM Vol WHERE origin LIKE %s"
        parameters=[param]
        cursor.execute(query, parameters)
        results = cursor.fetchall()
        context = {'results': results}
        return render(req, template_name, context) 
        
          
         
def filtervol(req, param):
    cursor = connection.cursor()
    if req.method == "GET":
            query = "SELECT * FROM Vol WHERE origin LIKE %s"
            parameters=[param]
            template_name='vols/galerieVol.html'
            cursor.execute(query, parameters)
            results = cursor.fetchall()
            context = {'results': results}
            return render(req, template_name, context)
            
def reserver(request):
    dateres = timezone.now()
    context = {'dateres': dateres}
    return render(request, 'vols/payerReservation.html', context) 
    
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


