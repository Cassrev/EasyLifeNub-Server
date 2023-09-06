from django.db import models

class GameGenre(models.Model):
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    genre_id = models.ForeignKey("Genre", on_delete=models.CASCADE)