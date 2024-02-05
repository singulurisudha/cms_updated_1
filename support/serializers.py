# # serializers.py
# from rest_framework import serializers
# from .models import Ticket
# from rest_framework.permissions import IsAuthenticated, IsAdminUser

# class TicketSerializer(serializers.ModelSerializer):
#     created_by = serializers.CharField(max_length=120, read_only=True)
#     solution = serializers.CharField(write_only=True, required=False)
#     updated_by = serializers.CharField(max_length=120,read_only=True)
#     class Meta:
#         model = Ticket
#         fields = ['id', 'issue', 'description', 'created_at', 'updated_at', 'status', 'created_by', 'solution','updated_by']

#     # Add the permission_classes attribute to specify permissions for the serializer
#     permission_classes = [IsAuthenticated]

#     def get_created_by(self, obj):
#         if obj and obj.created_by:
#             return obj.created_by.username  # Return the username instead of just accessing it

#     def create(self, validated_data):
#         # Check if the user is authenticated before creating the ticket
#         if self.context['request'].user.is_authenticated:
#             validated_data['created_by'] = self.context['request'].user

#             if validated_data.get('solution'):
#                 raise serializers.ValidationError("User can't create solution for the issue...")
#             return Ticket.objects.create(**validated_data)
#         else:
#             raise serializers.ValidationError("User must be authenticated to create a ticket.")

#     def update(self, instance, validated_data):
#         # Check if the user is authenticated before updating the ticket
#         if self.context['request'].user.is_authenticated:
#             # Ensure that only the 'solution' and 'status' fields can be updated
#             if 'solution' in validated_data:
#                 instance.solution = validated_data.get('solution')
#                 instance.status = 'resolved'
#                 instance.updated_by = self.context['request'].user
#                 instance.save()
#             return instance
#         else:
#             raise serializers.ValidationError("User must be authenticated to update a ticket.")
        

#     def validate(self, data):
#         user = self.context['request'].user

#         # Check if the user is an admin when trying to post a solution
#         if user and user.is_staff and 'solution' in data:
#             return data
#         elif 'solution' in data:
#             raise serializers.ValidationError("Only admin users can post solutions.")

#         return data

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         user = self.context['request'].user

#         # Only include the "solution" field if the user is an admin
#         if user and user.is_staff:
#             return data
#         else:
#             # Exclude the "solution" field for non-admin users
#             data.pop('solution', None)
#             return data



# serializers.py
from rest_framework import serializers
from .models import Ticket
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class TicketSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(max_length=120, read_only=True)
    solution = serializers.CharField(allow_blank=True, required=False)
    updated_by = serializers.CharField(max_length=120,read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'issue', 'description', 'created_at', 'updated_at', 'status', 'created_by', 'solution','updated_by']

    # Add the permission_classes attribute to specify permissions for the serializer
    permission_classes = [IsAuthenticated]

    def get_updated_by(self, obj):
        if obj and obj.updated_by:
            return obj.updated_by.username

    def get_created_by(self, obj):
        if obj and obj.created_by:
            return obj.created_by.username  # Return the username instead of just accessing it

    def create(self, validated_data):
        # Check if the user is authenticated before creating the ticket
        if self.context['request'].user.is_authenticated:
            validated_data['created_by'] = self.context['request'].user

            # # Check if a solution is provided and update the status accordingly
            # if 'solution' in validated_data and validated_data['solution']:
            #     validated_data['status'] = 'resolved'

            return Ticket.objects.create(**validated_data)
        else:
            raise serializers.ValidationError("User must be authenticated to create a ticket.")

    def update(self, instance, validated_data):
        # Check if the user is authenticated before updating the ticket
        if self.context['request'].user.is_authenticated:
            instance.issue = validated_data.get('issue', instance.issue)
            instance.description = validated_data.get('description', instance.description)
            instance.solution = validated_data.get('solution', instance.solution)

            # Update status to "resolved" if a solution is provided
            if instance.solution:
                instance.status = 'resolved'

            instance.save()
            return instance
        else:
            raise serializers.ValidationError("User must be authenticated to update a ticket.")

    def validate(self, data):
        user = self.context['request'].user

        # Check if the user is an admin when trying to post a solution
        if user and user.is_staff and 'solution' in data:
            return data
        elif 'solution' in data:
            raise serializers.ValidationError("Only admin users can post solutions.")

        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = self.context['request'].user

        # Only include the "solution" field if the user is an admin
        if user and user.is_staff:
            return data
        else:
            # Exclude the "solution" field for non-admin users
            data.pop('solution', None)
            return data