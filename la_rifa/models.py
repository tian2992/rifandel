from django.db import models

# Create your models here.


class Chance(models.Model):
    """A number or bet a person chooses for a raffle."""
    selection = models.IntegerField()
    user = models.User()

class Raffle(models.Model):
    name = models.CharField()

