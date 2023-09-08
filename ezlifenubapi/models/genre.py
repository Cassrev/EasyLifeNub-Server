from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=500)
    games = models.ManyToManyField("Game", through = "GameGenre")