from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    genres = models.ManyToManyField("Game", through='GameGenre')
    title = models.CharField(max_length=975)