# urls.py
from django.urls import path
from .views import MenuItemListCreateAPIView, MenuItemRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('menu-items/', MenuItemListCreateAPIView.as_view(), name='menu-item-list-create'),
    path('menu-items/<int:pk>/', MenuItemRetrieveUpdateDestroyAPIView.as_view(), name='menu-item-detail'),
]
