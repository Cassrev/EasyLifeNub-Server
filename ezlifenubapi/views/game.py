from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from ezlifenubapi.models import Game, Genre, GameGenre

class GameView(ViewSet):
    def retrieve(self, request, pk):
        game = Game.objects.get(pk=pk)

        serializer = GameSerializer(game)
        return Response(serializer.data)

    def list(self, request):
        games = Game.objects.all()

        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

class GameSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Game
        fields = ('id', 'genres', 'title')