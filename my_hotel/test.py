from django.db import models
import requests
import json
# import mysql.connector
import MySQLdb
conn = MySQLdb.connect(db='amadeus',user='Moussa',passwd='root',host='localhost',port='3306')
cursor = conn.cursor()

url = 'https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city?cityCode=PAR&radius=5&radiusUnit=KM&hotelSource=ALL'
token = 'SWnX7s5gy22gZPefIMedSb8epGgZ'
headers = {
    'Authorization': f'Bearer{token}'
}

# Envoi de la requete au niveau de API
response = requests.get(url,headers=headers)

# verification de la réponse du méthode get()
if response .status_code == 200:
    # conversion de la réponse en JSON
    data = response.json()
    # récupération des données de l'API
    hotels = data.get('data',[])
    # insérer les données dans la table de la base de données
    for hotel in hotels:
        print(hotel)
else:
    print("404")

