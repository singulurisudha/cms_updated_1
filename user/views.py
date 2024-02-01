from rest_framework import generics
from django.contrib.auth.models import User
from .models import Role, Permission, Module
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from .serializers import (UserLoginSerializer,RoleSerializer, 
                          PermissionSerializer, ModuleSerializer , 
                          UserRegistrationSerializer,ForgetPasswordUpdateSerializer)


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            # Use filter to get a queryset of users with the given email
            users = User.objects.filter(email=email)

            if users.exists():
                user = users.first()

                # Check the password for the first user in the queryset
                if user.check_password(password):
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'tokens': {
                            'access': str(refresh.access_token),
                            'refresh': str(refresh)
                        }
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({"detail": "Password is incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"detail": "Email is incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        serializer = ForgetPasswordUpdateSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(email=email)

                # Reset the password
                user.set_password(password)
                user.save()

                return Response({"detail": "Password reset successfully"}, status=status.HTTP_200_OK)

            except User.DoesNotExist:
                return Response({"detail": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RoleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class PermissionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class ModuleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
