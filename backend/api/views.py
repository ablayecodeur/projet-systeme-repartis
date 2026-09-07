from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from .models import Utilisateur, Produit
from .serializers import UtilisateurSerializer, ProduitSerializer

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer


@api_view(['GET'])
def health(request):
    """Liveness/readiness check: confirms the API responds and the
    database connection is reachable."""
    try:
        connection.ensure_connection()
        db_status = "ok"
    except Exception:
        db_status = "unreachable"

    status_code = 200 if db_status == "ok" else 503
    return Response({"status": "ok", "database": db_status}, status=status_code)