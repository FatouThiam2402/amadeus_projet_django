#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 09:08:23 2023

@author: kala
"""

from django.db import models

 
  # try:
  #     import django
  # except Exception:
  #     !pip install django
 
 
import requests
import json
# import mysql.connector

# import mysql.connector


# conn = mysql.connector.connect(db='amadeus',user='Moussa',passwd='root123',host='localhost',port=3306)
# cursor = conn.cursor()

url='https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city?cityCode=DKR&radius=300&radiusUnit=KM&hotelSource=ALL'
token = 'FuD2AyM2HgrAaKY4TPlHn2MS8Dfw'
headers = {
    'Authorization': f'Bearer {token}'
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
    i=0

    with open('insert_adresse_hotel.sql','w+') as f:
        for hotel in hotels:
            i+=1
            requete = """
                insert into Adresse(nomVille,pays,latitude,longitude) values('{}','{}','{}','{}');
            """.format(hotel['iataCode'],hotel['address']['countryCode'],hotel['geoCode']['latitude'],hotel['geoCode']['longitude'])
           
            f.write(requete)

            requete = """
                insert into Hotel(idHotel,nom,adresse_id,service_id) values('{}','{}','{}','{}');
            """.format(hotel['hotelId'],hotel['name'],i,3)
            f.write(requete)

        f.close()

else:
    print("impossible d\ny acceder")



