#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 22:58:26 2023

@author: kala
"""

import pandas as pd 

file = '/home/kala/Desktop/Flight-master/Data/airports.csv'

df = pd.read_table(file, header=0, sep=',')
ida = []
for idaer in df['code'] :
    ida.append(idaer)
    
print(ida)
    
nap = []
for k in df['airport'] :
    nap.append(k)
    
ct = []
for k in df['city'] :
    ct.append(k)

py = []
for k in df['country'] :
    py.append(k)    
    
for i in range(len(df)) : 
    with open('aeroport.sql', 'a+') as aero :
        query = """ INSERT INTO Aeroport (id_aero,nom_aero, ville,pays) VALUES ("{}","{}","{}","{}");""".format(ida[i], nap[i], ct[i], py[i])
        aero.write(query)
        i+=1;
