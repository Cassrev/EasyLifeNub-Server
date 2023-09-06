from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    dev_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_developers')
    genre = models.ManyToManyField("Game", through='GameGenre')
    title = models.CharField(max_length=975)