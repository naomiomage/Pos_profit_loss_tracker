from django.shortcuts import render
from rest_framework import generics, status, permissions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer


# ✅ Register user (open to anyone)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # anyone can register


# ✅ Simple login (no JWT required)
@api_view(['POST'])
def simple_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        return Response({
            "message": "Login successful",
            "username": user.username,
            "user_id": user.id
        }, status=status.HTTP_200_OK)
    else:
        return Response(
            {"error": "Invalid username or password"},
            status=status.HTTP_401_UNAUTHORIZED
        )
