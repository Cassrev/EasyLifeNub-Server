from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from ezlifenubapi.models import Game, IssueGameTicket

class TicketView(ViewSet):
    def retrieve(self, request, pk):
        ticket = IssueGameTicket.objects.get(pk=pk)
        serializer = GameTicketSerializer(ticket)
        return Response(serializer.data)

    def list(self, request):
        user = request.user
        tickets = IssueGameTicket.objects.filter(qa=user)

        if "user" in request.query_params:
            if request.query_params['user'] != "current":
                pk = request.query_params['user']
                tickets = tickets.filter(qa=pk)
        else:
            tickets = IssueGameTicket.objects.all()

        serializer = GameTicketSerializer(tickets, many=True)
        return Response(serializer.data)


    def create(self, request):
        token = request.auth

        qa = User.objects.get(auth_token=token)
        game = Game.objects.get(pk=request.data["game"])

        ticket = IssueGameTicket.objects.create(
            qa=qa,
            game=game,
            issue_title=request.data["issue_title"],
            bug_description=request.data["bug_description"],
            expected_result=request.data["expected_result"],
            repeat_step=request.data["repeat_step"]
        )
        serializer = GameTicketSerializer(ticket)
        return Response(serializer.data)

    def update(self, request, pk):

        ticket = IssueGameTicket.objects.get(pk=pk)
        ticket.issue_title = request.data["issue_title"]
        ticket.bug_description = request.data["bug_description"]
        ticket.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        ticket = IssueGameTicket.objects.get(pk=pk)
        ticket.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class QaTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'username')

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title')

class GameTicketSerializer(serializers.ModelSerializer):
    game = GameSerializer(many=False)
    qa = QaTicketSerializer(many=False)
    class Meta:
        model = IssueGameTicket
        fields = ('id', 'qa', 'game', 'issue_title', 'bug_description', 'expected_result', 'repeat_step')