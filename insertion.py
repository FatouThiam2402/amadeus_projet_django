import json
with open('donnees_voitures.json','r') as fichier:
    autodata=json.load(fichier)
with open('insertion_voiture.sql','w+') as f:
    for voiture in autodata:
        requette="""
        insert into  Voiture(marque,modele,nombre_places,boite_vitesse,carburant,climatisation,couleur,annee_production,prix,id_Service,image) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');
        """.format(voiture['marque'],voiture['modele'],voiture['nombre_places'],voiture['boite_vitesse'],voiture['carburant'],voiture['climatisation'],voiture['couleur'],voiture['annee_production'],voiture['prix'],'2',voiture['img'])
        f.write(requette)
    f.close()