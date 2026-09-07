from django.test import TestCase


class HealthCheckTests(TestCase):
    def test_health_endpoint_returns_ok(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")


class ProduitEndpointTests(TestCase):
    def test_liste_produits_returns_200(self):
        response = self.client.get("/api/produits/")
        self.assertEqual(response.status_code, 200)

    def test_liste_produits_est_vide_par_defaut(self):
        response = self.client.get("/api/produits/")
        self.assertEqual(response.json(), [])
