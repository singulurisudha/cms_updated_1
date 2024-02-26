from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from .serializers import (UserRegistrationSerializer,UserLoginSerializer)

from rest_framework import status
from .serializers import (UserLoginSerializer, 
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

                    return Response({'msg':{"Successfully Logged In ": '200 OK'},
                         

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

        serializer = UserLoginSerializer(data=request.data)

        serializer = ForgetPasswordUpdateSerializer(data=request.data)


        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(email=email)

                # Reset the password
                user.set_password(password)
                user.save()

                return Response({'msg':{"Success : ", 200},"detail": "Password reset successfully"}, status=status.HTTP_200_OK)

                return Response({"detail": "Password reset successfully"}, status=status.HTTP_200_OK)


            except User.DoesNotExist:
                return Response({"detail": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

