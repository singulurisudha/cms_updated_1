from rest_framework import generics
from menu.models import MenuItem
from menu.serializers import MenuItemSerializer

class MenuItemCreateAPIView(generics.CreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
