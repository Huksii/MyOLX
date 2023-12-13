from rest_framework import viewsets, permissions

from .models import Category, Ads
from .serializers import CategorySerializer, AdsSerializer

class AdsViewSet(viewsets.ModelViewSet):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [permissions.AllowAny]
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]