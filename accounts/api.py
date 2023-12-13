from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, SearchFilter

from django.contrib.auth.models import User
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    # select * from profile
    queryset = Profile.objects.all()
    
    # "__all__" 
    serializer_class = ProfileSerializer
    
    permission_classes = [permissions.AllowAny]
#permissions.IsAdminUser, permissions.IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    permission_classes = [permissions.AllowAny]