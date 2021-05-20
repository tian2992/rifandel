from django.test import TestCase
from django.utils import timezone
import la_rifa.models
import la_rifa.logic


# Create your tests here.

# models test
class RifaTest(TestCase):

    def create_Rifa(self, title="only a test", body="yes, this is only a test"):
        ri = la_rifa.models.Raffle(name="la rifa de pedrito", created_at=timezone.now())
        ri.save()
        return ri


    def test_whatever_creation(self):
        self.create_Rifa()
        r = la_rifa.models.Raffle.objects.first()

        self.assertTrue(isinstance(r, la_rifa.models.Raffle))
        self.assertEqual("la rifa de pedrito", r.name)
        return r


    def test_assign_bet(self):
        self.create_Rifa()
        r = la_rifa.models.Raffle.objects.first()

        la_rifa.logic.assign_bet(r, 23)


    def test_check_for_bet(self):
        self.create_Rifa()
        r = la_rifa.models.Raffle.objects.first()

        la_rifa.logic.assign_bet(r, 23)
        self.assertIsNotNone(la_rifa.logic.check_for_bet(r, 23))

