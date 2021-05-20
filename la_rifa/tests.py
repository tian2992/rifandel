from django.test import TestCase
from django.utils import timezone
import la_rifa.models


# Create your tests here.

# models test
class RifaTest(TestCase):

    def create_Rifa(self, title="only a test", body="yes, this is only a test"):
        return la_rifa.models.Raffle(name="la rifa de pedrito", created_at=timezone.now())

    def test_whatever_creation(self):
        r = self.create_Rifa()
        self.assertTrue(isinstance(r, la_rifa.models.Raffle))
        self.assertEqual("la rifa de pedrito", r.name)