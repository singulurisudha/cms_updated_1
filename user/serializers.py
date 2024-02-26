from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ('username', 'email', 'password', 'is_staff')
=======
        fields = ('username', 'email', 'password','is_staff')
>>>>>>> 1103a6d72f00a37c7610cfaf2dd1621e0293f610
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data.get('is_staff'):
            superuser = User.objects.create_superuser(**validated_data)
            return superuser
        else:
            user = User.objects.create_user(**validated_data)
            return user

<<<<<<< HEAD
    


=======
>>>>>>> 1103a6d72f00a37c7610cfaf2dd1621e0293f610
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

<<<<<<< HEAD



=======
class ForgetPasswordUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
>>>>>>> 1103a6d72f00a37c7610cfaf2dd1621e0293f610

