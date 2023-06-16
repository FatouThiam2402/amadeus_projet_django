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
from datetime import datetime, timedelta
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime, timedelta
# from xhtml2pdf import pisa


# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html  = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None
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
 	
 

 	

def toutLesVols(request):
    template_name = 'vols/voldispo.html'
    cursor = connection.cursor()
    origin = request.POST.get('origin')
    destination = request.POST.get('destination')
    departureDate = request.POST.get('departureDate')
    trip_type = request.POST.get('TripType')
    classe = request.POST.get('cabin')
    
    if request.method == "POST":
        if origin != '' or destination != '':
            query = "SELECT * FROM Vol WHERE origin LIKE %s AND destination LIKE %s"
            parameters = ('%' + origin + '%', '%' + destination + '%')
            cursor.execute(query, parameters)
            queryset = cursor.fetchall()
            if len(queryset) == 0:
                flightdatas = 'no info'
                context = {'objets': flightdatas}
                return render(request, 'vols/voldispo.html', context)
        else:
            messages.error(request, 'Aucune donnée soumise')
            return render(request, 'vols/choixvol.html')
    else:
        queryset = []  # Empty list if not a POST request

    paginator = Paginator(queryset, 5)  # Nombre d'objets par page
    page_number = request.GET.get('page')  # Récupérer le numéro de page depuis les paramètres de requête
    objets = paginator.get_page(page_number)
    context = {'objets': objets, 'origin': origin, 'destination': destination, 'depart': departureDate, 'classe': classe}
    return render(request, template_name, context)




def paiement(request, idvol, villedpt, hdpt, harriv, siegedispo, compagnie, prix, numvol):
    if request.user.is_authenticated:
        hdpt = str(timedelta(seconds=48600))
        harriv = str(timedelta(seconds=55800))
        context = {
            'idvol': idvol,
            'villedpt': villedpt,
            'hdpt': hdpt,
            'harriv': harriv,
            'siegedispo': siegedispo,
            'compagnie': compagnie,
            'prix': prix,
            'numvol': numvol
        }
        return render(request, 'vols/paiement.html', context)
    else:
        return HttpResponseRedirect(reverse("seConnecter"))
       
            
class galerie_vol(ListView):
    cursor = connection.cursor()
    template_name = 'vols/galerieVol.html'
    query = "SELECT DISTINCT(ville), pays, codeVille, imagedesc, latitude, longitude  FROM Localisation ORDER BY ville"
    cursor.execute(query)
    queryset = cursor.fetchall()
    paginate_by = 8
    
 
def voirdestination(request, param):
    cursor = connection.cursor()
    template_name = 'vols/voldispo.html'
    query = "SELECT * FROM Vol WHERE destination LIKE %s"
    parameters = [param]
    cursor.execute(query, parameters)
    queryset = cursor.fetchall()
    paginator = Paginator(queryset, 4)  # Nombre d'objets par page
    page_number = request.GET.get('page')  # Récupérer le numéro de page depuis les paramètres de requête
    objets = paginator.get_page(page_number)
    
    if (len(queryset) > 0) :
        return render(request, template_name, {'objets': objets})
    else :
        return render(request, template_name, {'nodestination': "Aucune destination n'est disponible pour le moment"})

          
         
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
        
from django.http import JsonResponse

def reserverVOYAGE(request):
        libelle = {}
        template_name='vols/reservation.html'
        cursor = connection.cursor()
    # if request.method == 'POST':
        if request.user.is_authenticated:
            # idc = user.id
            userid = request.POST.get('useridclt')
            userc = request.POST.get('user')
            numvol = request.POST.get('numvol')
            client = request.POST.get('client')
            depart = request.POST.get('hdpt')
            arrivee = request.POST.get('harr')
            sieges = request.POST.get('sdisp')
            siegeRes= request.POST.get('sres')
            prix = request.POST.get('pricing')
            dateres = datetime.now()
            lastdate = dateres + timedelta(days=15)
            devise = request.POST.get('devise')
            methodpay = request.POST.get('payment-method')
            messages.success(request, 'Reservation Reussie')
            libelle={'numvol': numvol, 'depart':depart,'arrivee': arrivee}
            libelle = str(libelle)
            context = {
                'id' : userc,
                'prix' : prix , 
                'numvol' : numvol,
                'client' : client,
                'depart' : depart,
                'arrivee' : arrivee,
                'sieges' : siegeRes,
                'dateres' : dateres,
                'paie':methodpay
            }
            query = "INSERT INTO Reservation (dateReservation, devise, montantTotal, siegeReserve , Client_id, Service_id, operateur, libelle ,dateAnnulation ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            parameters = (dateres, devise, prix, siegeRes, userid, 1, methodpay, libelle, lastdate)
            cursor.execute(query, parameters)
            connection.commit()

            return render(request, template_name, context)
        
def creerRapport(request):
    ref = request.GET.get("ref")
    ticket1 = Ticket.objects.get(ref_no=ref)
    data = {
        'ticket1':ticket1,
        'current_year': datetime.now().year
    }
    pdf = render_to_pdf('flight/ticket.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def monProfile(req, param):
    if req.user.is_authenticated:
        template_name='vols/profil.html'
        cursor = connection.cursor()
        query="select * from auth_user where id=%s"
        parameters=[param]
        cursor.execute(query, parameters)
        profile = cursor.fetchall()
        print(profile)
        return render(req, template_name, {'profile':profile})
    

            
def voirereservations(request, param):
    if request.user.is_authenticated:
        template_name='vols/toutmesreservations.html'
        libelles = []
        cursor = connection.cursor()
        query="select * from Reservation where Client_id=%s"
        parameters=[param]
        cursor.execute(query, parameters)
        results = cursor.fetchall()
        if(len(results) > 0) : 
            for row in results:
                # lbl = json.loads(str(row[8]))
                lbl = row[8]
                # print(json.loads(lbl))
                libelles.append(lbl)
            return render(request, template_name, {'reservations':results,'libelles':libelles[0]}) 
        else :
            return render(request, template_name, {'messagereserve':'Aucune reservation n est faite'}) 
        
def modifierreservations(request, param):
    if request.user.is_authenticated:
        template_name='vols/modification.html'
        libelles = []
        cursor = connection.cursor()
        query="select * from Reservation where Client_id=%s"
        parameters=[param]
        cursor.execute(query, parameters)
        results = cursor.fetchall()
        if(len(results) > 0) : 
            for row in results:
                # lbl = json.loads(str(row[8]))
                lbl = row[8]
                # print(json.loads(lbl));
                libelles.append(lbl)
            return render(request, template_name, {'reservations':results,'libelles':libelles[0]}) 
        else :
            return render(request, template_name, {'messagereserve':'Aucune reservation n est faite'}) 


# def misajour(request, param) : 
#       if request.method == "POST" :
          
         
    
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


