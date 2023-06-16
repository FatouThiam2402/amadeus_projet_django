from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
# import mysql.connector as sql

# connection = sql.connect(
# 	host='localhost',
# 	user='Moussa',
# 	password='root123',
# 	database='amadeus'
# )

# Create your views here.

def index(request) :
	

	# Créer un objet curseur
	with connection.cursor() as cursor:

	# Exécuter une requête SQL
		requette=""

		cursor.execute("SELECT * FROM Voiture;")

	# Récupérer les résultats de la requête
		results = cursor.fetchall()

	# # Parcourir les résultats
	# for row in results:
	# 	# Traiter chaque ligne de résultat
	# 	print(row)

	# Fermer le curseur
	
		return render(request, 'location_voiture/html_voiture.html',{'voitures':results})
	

	# reservation
def process_reservation(request):
	if request.method == 'post':
			field1_value = request.POST.get['pickup_location']
			field2_value = request.POST.get['return_location']
			field3_value = request.POST.get['vehicle_type']
			field4_value = request.POST.get['passenger_count']
			field5_value = request.POST.get['marque']
			field6_value = request.POST.get['prix']
			field7_value = request.POST.get['modele']
			field8_value = request.POST.get['couleur']
			field9_value = request.POST.get['additional_options']
			mes_valeurs=[field3_value,field4_value,field5_value,field7_value,field8_value,field9_value]
	
			requette="""INSERT INTO Reservation (dateReservation,Date_retour,prixReservation,Reserve_voiture)
			VALUES (field1_value,field2_value,field6_value,mes_valeurs)"""
			with connection.cursor() as cursor:
				cursor.execute(requette)
			resultats = cursor.fetchall()
			context = {'voitures' : resultats}
			# Faites quelque chose avec les valeurs récupérées

			return render(request, 'html_voiture.html', context)
	else:
		
		return render(request, 'html_voiture.html')
	
def process_recuper(request):
		# if request.method == 'post':
			# field1_value = request.POST.get['pickup_location']
			# field2_value = request.POST.get['return_location']
			# field3_value = request.POST.get['vehicle_type']
			field4_value = request.POST.get['passenger_count']
			field5_value = request.POST.get['marque']
			# field6_value = request.POST.get['prix']
			# field7_value = request.POST.get['modele']
			# field8_value = request.POST.get['couleur']
			# field9_value = request.POST.get['additional_options']
			# requette="""SELECT * FROM  Voiture WHERE nombre_places = %d OR marque = %s OR prix = %d OR modele = %s OR couleur = %s)
			
			# """
			requette="""SELECT * FROM Voiture WHERE nombre_places=3"""
			# parameters=[field3_value,field4_value,field5_value,field6_value,field7_value,field8_value]
			parameters=[field4_value]
			print(requette)
			cursor = connection.cursor() 
			cursor.execute(requette, parameters)	
			results = cursor.fetchall()
			print(results)	
			# Faites quelque chose avec les valeurs récupérées

			return render(request, 'location_voiture/html_voiture.html', {'voitures':results})
	# else:
		
		# return render(request, 'location_voiture/html_voiture.html')
	

	

	





