#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 19:22:26 2023

@author: kala
"""
from tqdm import tqdm
from datetime import timedelta, datetime
import pandas as pd
import random

numbers = [1, 2, 3, 4, 5 , 6, 7 , 8, 9, 10]

def get_number_of_lines(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def addInternationalFlights():
    k = 1;
    file = open("international_flights.csv", "r")
    print("Adding International Flights...")
    total = get_number_of_lines("international_flights.csv")
    for i, line in tqdm(enumerate(file), total=total):
        if i == 0:
            continue
        data = line.split(',')
        origin = data[1].strip()
        destination = data[2].strip()
        depart_time = datetime.strptime(data[3].strip(), "%H:%M:%S").time()
        depart_week = int(data[4].strip())
        duration = timedelta(hours=int(data[5].strip()[:2]), minutes=int(data[5].strip()[3:5]))
        arrive_time = datetime.strptime(data[6].strip(), "%H:%M:%S").time()
        arrive_week = int(data[7].strip())
        flight_no = data[8].strip()
        idavion = data[9].strip()
        airline = data[10].strip()
        economy_fare = float(data[11].strip()) if data[11].strip() else 0.0
        business_fare = float(data[12].strip()) if data[12].strip() else 0.0
        first_fare = float(data[13].strip()) if data[13].strip() else 0.0
            # df = df.assign(origin=org)
        
        try:
            idv = 1;
            with open('volsql.sql', 'a+') as aero :
                sr = random.choice(numbers)
                query = """ INSERT INTO Vol (idVol,siegeReservables, Service_id, origin, destination, depart , arrivee, jourdepart, duree, compagnieAerienne, avion, prixECONOMY , prixBUSINESS, prixFIRST, jourarrivee, numero) VALUES ({},{},{},"{}","{}","{}","{}",{},"{}","{}","{}","{}","{}","{}",{},"{}");\n""".format(k,sr,idv,origin,destination,depart_time, arrive_time, depart_week, duration, airline,idavion, economy_fare, business_fare, first_fare, arrive_week,flight_no )
                aero.write(query)
                k+=1;
             # a1 = Flight.objects.create(origin=Place.objects.get(code=origin), destination=Place.objects.get(code=destination), depart_time=depart_time , duration=duration, arrival_time=arrive_time, plane=flight_no, airline=airline, economy_fare=economy_fare, business_fare=business_fare, first_fare=first_fare)
        #     a1.depart_day.add(Week.objects.get(number=depart_week))
        #     a1.save()
        except Exception as e:
             print(e)
             return
    print("Done.\n")
    
    
df = addInternationalFlights()