#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 23:32:17 2023

@author: kala
"""


# | idVol             | int          | NO   | PRI | NULL    | auto_increment |
# | siegeReservables  | int          | YES  |     | NULL    |                |
# | Service_id        | int          | YES  | MUL | NULL    |                |
# | origin            | varchar(200) | YES  |     | NULL    |                |
# | destination       | varchar(200) | YES  |     | NULL    |                |
# | depart            | datetime     | YES  |     | NULL    |                |
# | arrivee           | datetime     | YES  |     | NULL    |                |
# | jourdepart        | date         | YES  |     | NULL    |                |
# | duree             | time         | YES  |     | NULL    |                |
# | compagnieAerienne | varchar(200) | YES  |     | NULL    |                |
# | avion             | varchar(200) | YES  |     | NULL    |                |
# | prixECONOMY       | double       | YES  |     | NULL    |                |
# | prixBUSINESS      | double       | YES  |     | NULL    |                |
# | prixFIRST         | double       | YES  |     | NULL    |                |
# | jourarrivee       | date         | YES  |     | NULL   

import pandas as pd 
import random

numbers = [0, 1, 2, 3, 4, 5 , 6, 7 , 8, 9, 10]

file = '/home/kala/Desktop/Flight-master/Data/international_flights.csv'

df = pd.read_table(file, header=0, sep=',')
org = []
for k in df['origin'] :
    org.append(k)
    
dest = []
for k in df['destination'] :
    dest.append(k)

dpt = []
for k in df['depart_time'] :
    dpt.append(k)
    
dwd = []
for k in df['depart_weekday'] :
    dwd.append(k)

dur = []
for k in df['duration'] :
    dur.append(k)

arr = []
for k in df['arrival_time'] :
    arr.append(k)
    
awd = []
for k in df['arrival_weekday'] :
    awd.append(k)
    
fln = []
for k in df['flight_no'] :
    fln.append(k)
    
airc = []
for k in df['airline_code'] :
    airc.append(k)
 
cmp = []
for k in df['airline'] :
    cmp.append(k)
    
eco = []
for k in df['economy_fare'] :
    eco.append(k)

bus = []
for k in df['business_fare'] :
    bus.append(k)

ffa = []
for k in df['first_fare'] :
    ffa.append(k)    
    
idv = 1;
for i in range(len(df)) : 
    sr = random.choice(numbers)
    with open('vol.sql', 'a+') as aero :
        query = """ INSERT INTO Vol (idVol,siegeReservables, Service_id, origin, destination, depart , arrivee, jourdepart, duree, compagnieAerienne, avion, prixECONOMY , prixBUSINESS, prixFIRST, jourarrivee, numero) VALUES ({},{},{},"{}","{}","{}","{}",{},"{}","{}","{}","{}","{}","{}",{},"{}");\n""".format(i,sr,idv,org[i],dest[i],dpt[i], arr[i], dwd[i], dur[i], cmp[i], airc[i], eco[i], bus[i], ffa[i], awd[i],fln[i] )
        aero.write(query)
        i+=1;
