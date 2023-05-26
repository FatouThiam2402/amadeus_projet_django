from django.db import models

 
  # try:
  #     import django
  # except Exception:
  #     !pip install django
 
 
import requests
import json
import mysql.connector

import mysql.connector


conn = mysql.connector.connect(db='amadeus',user='Moussa',passwd='root123',host='localhost',port=3306)
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
    
# with open('insertion.sql','w+') as f:
#     for hotel in hotels:
#         requete = """
    
#             insert into nom_table(attr1,attr2,attr3) values(hotel['name'],hotel['name'],hotel['name'])+'\n'
#         """
#         f.write(requete)

#     f.close()   


