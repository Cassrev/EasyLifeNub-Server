from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from ezlifenubapi.models import Game, Genre, GameGenre

class GameGenreView(ViewSet):
    def retrieve(self, request, pk):
        game_genre = GameGenre.objects.get(pk=pk)

        serializer = GameGenreSerializer(game_genre)
        return Response(serializer.data)

    def list(self, request):
        game_genre = GameGenre.objects.all()

        serializer = GameGenreSerializer(game_genre, many=True)
        return Response(serializer.data)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

class GameSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True, source='gamegenre_relationship.genre')
    
    class Meta:
        model = Game
        fields = ('id', 'genres', 'title')

class GameGenreSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=False)
    game = GameSerializer(many=False)

    class Meta:
        model = Game
        fields = ('id', 'genre', 'game')