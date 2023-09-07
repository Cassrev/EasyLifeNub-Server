from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from ezlifenubapi.models import Game, Genre

class GameView(ViewSet):
    def retrieve(self, request, pk):
        game = Game.objects.get(pk=pk)
        
        serializer = GameSerializer(game, context={'request': request})
        return Response(serializer.data)

    def list(self, request):
        game = Game.objects.all()

        serializer = GameSerializer(game, many=True)
        return Response(serializer.data)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'genre', 'title')