import mysql.connector 
baseDeDonnees = mysql.connector.connect(host="localhost",user="Moussa",password="root123", database="amadeus")
curseur = baseDeDonnees.cursor()

