from rest_framework.routers import DefaultRouter
from .views import UtilisateurViewSet, ProduitViewSet

router = DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'produits', ProduitViewSet)

urlpatterns = router.urls