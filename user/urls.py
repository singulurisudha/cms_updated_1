from django.urls import path
from .views import UserLoginView, UserRegistrationView,RoleListCreateAPIView, PermissionListCreateAPIView, ModuleListCreateAPIView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('roles/', RoleListCreateAPIView.as_view(), name='role-list-create'),
    path('permissions/', PermissionListCreateAPIView.as_view(), name='permission-list-create'),
    path('modules/', ModuleListCreateAPIView.as_view(), name='module-list-create'),
]
