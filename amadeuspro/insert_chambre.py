import json

with open('donnees_chambres.json','r') as fichier:

    chambres = json.load(fichier)

with open('insert_chambre.sql','w+') as f:
    for ch in chambres:

        requete = """
            insert into Chambre(nom_chambre,description,prix_chambre,image,idHotel) values('{}','{}','{}','{}',,'{}');
        """.format(ch['nom_chambre'],ch['description'],ch['prix_chambre'],ch['image'],ch['idhotel'])
        f.write(requete)

    f.close()




