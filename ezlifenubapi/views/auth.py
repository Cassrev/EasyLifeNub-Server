from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data['username']
    password = request.data['password']

    authenticated_user = authenticate(username=username, password=password)

    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key,
            'staff': authenticated_user.is_staff
        }
        return Response(data)
    else:
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    email = request.data.get('email', None)
    username = request.data.get('username', None)
    first_name = request.data.get('first_name', None)
    last_name = request.data.get('last_name', None)
    password = request.data.get('password', None)

    if email is not None \
        and first_name is not None \
        and last_name is not None \
        and password is not None:
        if email is None:
            return Response(
                {'message': 'You must provide an email'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if first_name is None:
            return Response(
                {'message': 'You have a first name. Where is it?'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if last_name is None:
                return Response(
                    {'message': 'No last name.'},
                    status=status.HTTP_400_BAD_REQUEST
                )            
        if password is None:
            return Response(
                {'message': 'You must provide a password'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            new_user = User.objects.create_user(
                username=request.data['username'],
                password=request.data['password'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                email = request.data['email']
            )
            new_user.save()

        except IntegrityError:
            return Response(
                {'message': 'An account with that email address already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )


        token = Token.objects.create(user=new_user)
        data = { 'token': token.key, 'staff': new_user.is_staff }
        return Response(data)
