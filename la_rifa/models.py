from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Raffle(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    runs_at = models.DateTimeField(null=True)


class Chance(models.Model):
    """A number or bet a person chooses for a raffle."""
    selection = models.IntegerField()
    raffle = models.ForeignKey(Raffle, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

