"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from ezlifenubapi.models import Game, IssueGameTicket

class TicketView(ViewSet):
    def retrieve(self, request, pk):
        ticket = Event.objects.get(pk=pk)
        serializer = GameTicketSerializer(ticket)
        return Response(serializer.data)

    def list(self, request):
        events = Event.objects.all()

        if "game" in request.query_params:
            game_id = request.query_params['game']
            events = events.filter(game_id=game_id)

        serializer = GameTicketSerializer(events, many=True)
        return Response(serializer.data)

    def create(self, request):
        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])

        event = Event.objects.create(
            host=gamer,
            game=game,
            event_name=request.data["event_name"]
        )
        serializer = GameTicketSerializer(event)
        return Response(serializer.data)

    def update(self, request, pk):

        event = Event.objects.get(pk=pk)
        event.event_name = request.data["event_name"]
        
        game = Game.objects.get(pk=request.data["game"])
        event.game = game
        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

# class EventHostSerializer(serializers.ModelSerializer):
#     """JSON serializer for games
#     """
#     class Meta:
#         model = Gamer
#         fields = ('id', 'user_name', 'bio')


class GameTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueGameTicket
        fields = ('id', 'game', 'issue_title', 'bug_description', 'expected_result', 'repeat_step')