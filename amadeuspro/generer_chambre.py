import json
import random
from  datetime import datetime,timedelta

idHotels = ["RDDKR117", "HSDKRAAL", "IQDKRTER", "TYDKRRAC","WKDKR563","TYDKRRHI","GWBJL253","SIBJL975","FGDKRLDN"]

descriptions = ["Une chambre spacieuse avec une vue panoramique sur la ville.",
               "Un havre de paix au cœur de la nature, idéal pour se détendre.",
               "Un mélange d'élégance et de confort pour un séjour inoubliable.",
               "Des équipements modernes et un décor raffiné pour un séjour luxueux.",
               "Une chambre accueillante et chaleureuse pour se sentir comme chez soi."
               ]

nom_chambres = ['Suite','Chambre Deluxe','Chambre Standard','Chambre Vue Mer','Chambre Familiale']

#générer prix chambre dans un interval donné
def generer_prix_chambre(min_prix, max_prix):

    return random.randint(min_prix, max_prix)

# liste  image des chambres
images = ["static/images/img_chambre/chambre1.jpg",
          "static/images/img_chambre/chambre2.jpg",
          "static/images/img_chambre/chambre3.jpg",
          "static/images/img_chambre/chambre4.jpeg",
          "static/images/img_chambre/chambre6.jpeg",
          "static/images/img_chambre/chambre7.jpg",
          "static/images/img_chambre/chambre8.jpg",
          "static/images/img_chambre/chambre9.jpg"
    
]





data_chambres = []
chambre = {}

for _ in range(100):
    idhotel = random.choice(idHotels)
    description = random.choice(descriptions)
    nom_ch = random.choice(nom_chambres)
    prix_ch = generer_prix_chambre(10000,50000)
    img = random.choice(images)

    chambre = {
        "nom_chambre":nom_ch,
        "description":description,
        "prix_chambre":prix_ch,
        "image":img,
        "idhotel": idhotel,
    
    }
  

    data_chambres.append(chambre)

with open("donnees_chambres.json", "w") as f:
    json.dump(data_chambres, f)