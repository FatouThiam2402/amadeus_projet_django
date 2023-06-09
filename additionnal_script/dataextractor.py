#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 10:40:25 2023

@author: kala
"""

import requests
import json
# import mysql.connector

# import mysql.connector


# conn = mysql.connector.connect(db='amadeus',user='Moussa',passwd='root123',host='localhost',port=3306)
# cursor = conn.cursor()

keyword = ['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for ky in keyword :
    requete = "";
    requete2 = "";
    url='https://test.api.amadeus.com/v1/reference-data/locations?subType=CITY&keyword='+ky+'&page%5Boffset%5D=0&sort=analytics.travelers.score&view=FULL'
    token = 'L71rzEjGxLzKpLT8OjU5mabyFLpr'
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
        Aeroports = data.get('data',[])
        # insérer les données dans la table de la base de données
        i=0
    
        for Aeroport in Aeroports:
                print(Aeroport)
                with open('insert_adresse.sql','a') as f:
                    i+=1
                    requete = """insert into Adresse(codeVille,ville, pays,latitude,longitude, zone) values('{}','{}','{}','{}','{}','{}');
                    """.format(Aeroport['iataCode'],Aeroport['address']['cityName'],Aeroport['address']['countryName'],Aeroport['geoCode']['latitude'],Aeroport['geoCode']['longitude'],Aeroport['address']['regionCode'])
                   
                    f.write(requete)
                with open('insert_aeroport.sql','a') as f:
                    requete2 = """insert into Aeroport(id_aero,nom_aero) values('{}','{}');
                    """.format(Aeroport['id'],Aeroport['name'])
                    f.write(requete2)
    
    
    else:
        print("impossible d\ny acceder")