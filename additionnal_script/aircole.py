#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 09:15:12 2023

@author: kala
"""

import requests
import json
import itertools

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

combinations = list(itertools.combinations(alphabet, 2))

for combination in combinations:
    aircode = ''.join(combination)

    url = "https://test.api.amadeus.com/v1/reference-data/airlines?airlineCodes="+aircode
    
    token = 'h5UgkFc1HWWMM4zdMsl5fiFjuvMa'
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
        comp = data.get('data',[])
        print(comp)
        # insérer les données dans la table de la base de données
        i=0
        with open('compagnie.sql','a') as f:
            for cp in comp:
                    i+=1
                    requete = """
                        insert into Compagnie(idcompagnie,code,nomCompagnie,Service_id) values({},'{}','{}','{}');
                    """.format(i, cp['iataCode'],cp['businessName'],1)
                   
                    f.write(requete)


            f.close()