from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom