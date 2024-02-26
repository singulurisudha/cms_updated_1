from django.urls import path
from .views import *


urlpatterns = [
    path('menu/', MenuItemListAPIView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', MenuItemRetrieveAPIView.as_view(), name='menu-detail'),

    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category-detail'),


    path('content/', ContentListAPIView.as_view(), name='content-list'),
    path('content/<int:pk>/', ContentRetrieveAPIView.as_view(), name='content-detail'),
    path('archived_content/<int:pk>/', ContentRetrieveAPIView.as_view(), name='content-detail'),


    path('support/', SupportListAPIView.as_view(), name='support-list'),
    path('support/<int:pk>/', SupportRetrieveAPIView.as_view(), name='support-detail'),
]
