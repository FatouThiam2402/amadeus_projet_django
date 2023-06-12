from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection


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
	def reservation(request,parametre):
		pass

		





