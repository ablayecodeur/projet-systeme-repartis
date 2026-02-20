from django.contrib import admin
from .models import Utilisateur, Produit

admin.site.register(Utilisateur)
admin.site.register(Produit)