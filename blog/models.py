from django.db import models
from django.conf import settings


class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)

    def occuper(self, animal):  # méthode d'objet
            if len(self.occupants) < self.capacité:
                self.occupants.append(animal)
                if len(self.occupants) == self.capacité:
                    self.disponibilité = 'occupé'
    def __str__(self):
        return self.id_equip


class Animal(models.Model):
    id_animal = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    race = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)


    def __str__(self):
        lieu.occuper(self)
        return self.id_animal
