#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 11:58:59 2023

@author: kala
"""
import requests, random
import json
from datetime import datetime, timedelta

# CREATE TABLE Vol (
#  	idVol  integer PRIMARY KEY auto_increment, , 
#  	payementRapide  bool  ,
#  	allerSimple  bool  ,  
#  	siegeReservables integer  , 
#  	AeroportDepart varchar(200),
#  	HeureDepart date  , 
#  	AeroportArrivee varchar(200),
#  	HeureArrivee date  , 
#  	Service_id integer  ,
#     Foreign key (Service_id) references TypeOffre(id)

# );
# CREATE USER 'Moussa'@'localhost' IDENTIFIED BY '!?00root123!?';
# GRANT ALL PRIVILEGES ON flat.* TO 'flatadmin'@'localhost';
# CREATE USER 'flatadmin'@'localhost' IDENTIFIED BY '!?00Root123!?';

# FLUSH PRIVILEGES;

air = ['ANC', 'LAX', 'SFO', 'SEA', 'LAS', 'DEN', 'SLC', 'PDX', 'FAI', 'MSP', 'PHX', 'SJU', 'PBG', 'IAG', 'PSE', 'BQN', 'ORD', 'GEG', 'HNL', 'ONT', 'MCO', 'BOS', 'HIB', 'ABR', 'MAF', 'DFW', 'MKE', 'IAH', 'BNA', 'BRO', 'VPS', 'BOI', 'BJI', 'SGF', 'PHL', 'SBN', 'RDD', 'EUG', 'IAD', 'BUF', 'PWM', 'JFK', 'CRP', 'PIA', 'FAT', 'SMF', 'AUS', 'MCI', 'ATL', 'JAX', 'MFR', 'IDA', 'MSN', 'DCA', 'SAT', 'CHS', 'SBA', 'SMX', 'IND', 'CLE', 'GSP', 'BDL', 'ABI', 'RIC', 'BFL', 'OMA', 'RDM', 'FLL', 'CID', 'TPA', 'SYR', 'ROC', 'TYR', 'LAN', 'XNA', 'GSO', 'EWR', 'PBI', 'RSW', 'OAK', 'PVD', 'RNO', 'PIT', 'ABQ', 'MSO', 'TTN', 'AMA', 'CLL', 'HOU', 'JLN', 'MLI', 'RDU', 'CVG', 'MHK', 'MOB', 'TLH', 'PNS', 'BHM', 'CAE', 'TXK', 'ACY', 'DTW', 'RAP', 'TUS', 'EAU', 'DLH', 'FSD', 'INL', 'CMX', 'SPI', 'CLD', 'COD', 'CMH', 'LRD', 'PSC', 'CPR', 'ACV', 'DAL', 'PAH', 'MRY', 'ESC', 'ISN', 'PSP', 'MFE', 'STL', 'BTV', 'FSM', 'AEX', 'SPS', 'ACT', 'SJT', 'JAN', 'OKC', 'FAR', 'MTJ', 'GCC', 'MSY', 'OGG', 'SJC', 'GUC', 'MIA', 'ORF', 'MOT', 'MLU', 'KOA', 'SAN', 'LGA', 'LAW', 'PIB', 'MEM', 'MGM', 'SBP', 'COS', 'LAR', 'DRO', 'BIS', 'ITO', 'ELP', 'HSV', 'DVL', 'ALB', 'CLT', 'SNA', 'BWI', 'ISP', 'MDW', 'EVV','DKR','PAR']

for i in range(3) :
    aircode = random.choice(air)
    aircode2 = random.choice(air)
    # aircode = 'BOS'
    # aircode2= 'PAR'
    # vol['itineraries'][0]['segments'][0]['departure']
    
    # Définir les bornes des dates
    # start_date = datetime(2023, 7, 1)
    # end_date = datetime(2023, 12, 31)
    
    # # Calculer la différence en jours
    # days_diff = (end_date - start_date).days
    
    # # Générer une date aléatoire
    # random_days = random.randint(0, days_diff)
    # ddpt = str(start_date + timedelta(days=random_days))
    # ddpt = str(ddpt)
    ddpt = "2023-07-01"

    
    # Afficher la date aléatoire
    
    
    if (aircode!=aircode2) :
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode="+aircode+"&destinationLocationCode="+aircode2+"&departureDate="+ddpt+"&adults=1&nonStop=false&max=250"
        token = "FwTMUIlfKHpRnSvmNTmWexwEoN7a"
        headers = {
                'Authorization': f'Bearer {token}'
        }
        response = requests.get(url,headers=headers)
        if response .status_code == 200:
            data = response.json()
            print(data)
            Vols = data.get('data',[])
            i=0
            sid = 1
            for vol in Vols:
                   
                    with open('insert_vol.sql','a+') as f:
                        segments =  vol['itineraries'][0]['segments'][0]
                        departs  = segments['departure']
                        arrivees = segments['arrival']
                        i+=1
                        requete = """insert into Vol(idVol, payementRapide, allerSimple, dernierTicketAchete, siegeReservables, AeroportDepart, HeureDepart, AeroportArrivee, HeureArrivee, Service_id) values({},'{}','{}',{},'{}','{}','{}','{}',{});
                        """.format(vol['id'],vol['instantTicketingRequired'],
                        vol['oneWay'], 
                        vol['lastTicketingDate'],
                        vol['numberOfBookableSeats'],
                        departs['iataCode'],
                        departs['at'],
                        arrivees['iataCode'],
                        arrivees['at'],
                        sid
                        )
                        f.write(requete)
                        
                    with open('insert_price.sql','a+') as f:
                         i+=1
                         pricing = vol['price'][0]
                         requete = """insert into Price(id, devise, total, grandTotal) values({},'{}');
                         """.format(vol['id'] , pricing['currency'],pricing['total'], pricing['grandTotal'])
                         f.write(requete)
                        
                    with open('insert_passager.sql','a+') as f:
                         i+=1
                         trav = vol['travelerPricings'][0]
                         requete = """insert into Passager(id, idPassager, typePassager) values({},'{}');
                         """.format(vol['id'],trav['travelerId'],trav['travelerType'])
                         f.write(requete)
        else:
            print("impossible d\ny acceder")
