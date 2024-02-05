from django.shortcuts import render
from rest_framework import generics
from menu.models import MenuItem
from support.views import *
from menu.serializers import MenuItemSerializer
from category.views import *

class MenuItemListAPIView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemRetrieveAPIView(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ContentListAPIView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class SupportListAPIView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class SupportRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

