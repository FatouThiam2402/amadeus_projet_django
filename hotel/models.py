from django.db import models


class Slider(models.Model):
    caption = models.CharField(max_length=150)
    slogan = models.CharField(max_length=120)
    image = models.ImageField(upload_to='sliders/')

    def __str__(self):
        return self.caption[:20]

    class Meta:
        verbose_name_plural = 'Slider'


# class Service(models.Model):
#     title = models.CharField(max_length=120)
#     description = models.TextField()
#     items = models.ManyToManyField(to='Item',)
#     thumbnail = models.ImageField(upload_to='services/')
#     cover = models.ImageField(upload_to='services/')
#     image1 = models.ImageField(upload_to='services/', blank=True, null=True)
#     image2 = models.ImageField(upload_to='services/', blank=True, null=True)

#     def __str__(self):
#         return self.title


class Item(models.Model):
    title = title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


# class Doctor(models.Model):
#     name = models.CharField(max_length=120)
#     speciality = models.CharField(max_length=120)
#     picture = models.ImageField(upload_to="doctors/")
#     details = models.TextField()
#     experience = models.TextField()
#     expertize = models.ManyToManyField(to='Expertize', related_name='doctors')
#     twitter = models.CharField(max_length=120, blank=True, null=True)
#     facebook = models.CharField(max_length=120, blank=True, null=True)
#     instagram = models.CharField(max_length=120, blank=True, null=True)

#     def __str__(self):
#         return self.name


# class Expertize(models.Model):
#     name = models.CharField(max_length=120)

#     def __str__(self):
#         return self.name


# class Faq(models.Model):
#     question = models.CharField(max_length=120)
#     answer = models.TextField()

#     def __str__(self):
#         return self.question


# class Gallery(models.Model):
#     title = models.CharField(max_length=120)
#     image = models.ImageField(upload_to="gallery/")

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name_plural = "Galleries"



class typeOffre(models.Model) :
  typeofr = models.CharField(max_length=200)
  def __str__(self):
        return self.typeofr

class client(models.Model) :
      nomComplet =  models.CharField(max_length=200)
      telephone =  models.CharField(max_length=200)
      email = models.CharField(max_length=200)
      adresse= models.CharField(max_length=200)
      dernierTicketAchete = models.DateField()
      def __str__(self):
        return self.nomComplet


class passager(models.Model) :
      nomPassager =  models.CharField(max_length=200)
      telephone =  models.CharField(max_length=200)
      email = models.CharField(max_length=200)
      genre = models.CharField(max_length=50)
      typePassager  = models.CharField(max_length=200)
      numeroCarte= models.CharField(max_length=200)
      Pointage= models.IntegerField()
      estblackliste = models.BooleanField()
      def __str__(self):
        return self.nomPassager


class compagnie(models.Model) :
      nomCompagnie =  models.CharField(max_length=200)
      def __str__(self):
        return self.nomCompagnie



class vol(models.Model) :
      typevol =  models.ForeignKey(typeOffre, on_delete=models.CASCADE)
      source =  models.CharField(max_length=200)
      achatInstantane = models.BooleanField()
      allerSimple = models.BooleanField()
      dernierAchat = models.DateField()
      nombreSiegeReserve =  models.IntegerField()
      dateDepart  = models.DateField()
      dateArrivee = models.DateField()

      def __str__(self):
            return self.typevol

class volGenerique(models.Model) :
    compagnie =  models.CharField(max_length=200)
    heureDepart  = models.DateField()
    heureArrivee = models.DateField()
    capacite =  models.IntegerField()
    aeroportDepart =  models.CharField(max_length=200)
    aeroportArrivee =  models.CharField(max_length=200)

    def __str__(self):
        return self.compagnie

class reservation(models.Model) :
      dateReservation =  models.DateField()
      nomclient = models.ForeignKey(client, on_delete=models.CASCADE)
      nomPassager = models.ForeignKey(passager, on_delete=models.CASCADE)
      nomvol = models.ForeignKey(vol, on_delete=models.CASCADE)
      prixReservation = models.IntegerField()
      devise = models.CharField(max_length=200)
      montantTotal = models.IntegerField()
      bagageInclus = models.BooleanField()
      def __str__(self):
        return self.nomclient

class ville(models.Model) :
      nomVille = models.CharField(max_length=200)
      pays= models.CharField(max_length=200)
      def __str__(self):
        return self.nomVille

class aeroport(models.Model) :
      nomAeroport = models.CharField(max_length=200)
      paysAeroport = models.ForeignKey(ville, on_delete=models.CASCADE)
      def __str__(self):
        return self.nomAeroport

class escale(models.Model) :
    lieuArret = models.ForeignKey(aeroport, on_delete=models.CASCADE)
    def __str__(self):
        return self.lieuArret



