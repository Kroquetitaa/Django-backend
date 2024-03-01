from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .serializers import SignUpSerializers, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.


@api_view(['POST'])
def register(request):
    data = request.data

    user = SignUpSerializers(data=data)

    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user = User.objects.create(
                first_name=data['first_name'],
                last_name=data['first_name'],
                username=data['email'],
                email=data['email'],
                password=make_password(data['password'])
            )
            return Response({
                'message': 'User registered'
            }, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def currentUser(request):
    user = UserSerializer(request.user)
    
    return Response(user.data)