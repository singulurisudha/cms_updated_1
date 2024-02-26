from rest_framework import generics
from .models import Category, Content
from .serializers import CategorySerializer, ContentSerializer

class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateDestroyAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ContentCreateAPIView(generics.CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContenUpdateDestroyAPIView(generics.UpdateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
