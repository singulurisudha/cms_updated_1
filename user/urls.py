from django.urls import path
from .views import UserLoginView, UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
<<<<<<< HEAD
    
=======
>>>>>>> 1103a6d72f00a37c7610cfaf2dd1621e0293f610
]
