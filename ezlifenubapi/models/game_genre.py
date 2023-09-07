from django.db import models

class GameGenre(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="gamegenre_relationship")
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE, related_name="gamegenre_relationship")