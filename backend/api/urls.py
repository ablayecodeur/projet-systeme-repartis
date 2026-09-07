from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UtilisateurViewSet, ProduitViewSet, health

router = DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'produits', ProduitViewSet)

urlpatterns = [
    path('health/', health, name='health'),
] + router.urls