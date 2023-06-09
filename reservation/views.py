from django.shortcuts import render
import mysql.connector

# Établir une connexion à la base de données
connection = mysql.connector.connect(
        host='localhost',
        user='Moussa',
        password='root123',
        database='amadeus'
)
def paiement(request, idvol, villedpt, datedpt, villearriv, siegedispo) :
        context = {'idvol': idvol, 'villedpt':villedpt, 'datedpt' : datedpt, 'villearriv': villearriv, 'siegedispo':siegedispo}
        return render(request, 'reservation/paiement.html', context)
# Create your views here.
