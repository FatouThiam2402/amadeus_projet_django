import json
import random
from  datetime import datetime,timedelta

idHotels = ["RDDKR117", "HSDKRAAL", "IQDKRTER", "TYDKRRAC","WKDKR563","TYDKRRHI","GWBJL253","SIBJL975","FGDKRLDN"]

descriptions = ["Une chambre spacieuse avec une vue panoramique sur la ville.",
               "Un havre de paix au cœur de la nature, ideal pour se detendre.",
               "Un melange d_elegance et de confort pour un sejour inoubliable.",
               "Des equipements modernes et un decor raffine pour un sejour luxueux.",
               "Une chambre accueillante et chaleureuse pour se sentir comme chez soi."
               ]

nom_chambres = ['Suite','Chambre Deluxe','Chambre Standard','Chambre Vue Mer','Chambre Familiale']

#générer prix chambre dans un interval donné
def generer_prix_chambre(min_prix, max_prix):

    return random.randint(min_prix, max_prix)

# liste  image des chambres
images = ["amadeuspro/images/img_chambre/chambre1.jpg", 
          "amadeuspro/images/img_chambre/chambre2.jpg",
          "amadeuspro/images/img_chambre/chambre3.jpg",
          "amadeuspro/images/img_chambre/Chambre6.jpeg",
          "amadeuspro/images/img_chambre/chambre7.jpg",
          "amadeuspro/images/img_chambre/chambre8.jpg",
          "amadeuspro/images/img_chambre/chambre9.jpg"
    
]




data_chambres = []
chambre = {}

for _ in range(100):
    idhotel = random.choice(idHotels)
    description = random.choice(descriptions)
    nom_ch = random.choice(nom_chambres)
    prix_ch = generer_prix_chambre(15000,100000)
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