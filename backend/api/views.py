from rest_framework import viewsets
from .models import Utilisateur, Produit
from .serializers import UtilisateurSerializer, ProduitSerializer

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer