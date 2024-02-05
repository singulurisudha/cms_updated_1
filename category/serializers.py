from rest_framework import serializers
from .models import Category, Content
from rest_framework.permissions import IsAuthenticated

class CategorySerializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated]

    class Meta:
        model = Category
        fields = ['id', 'category']

    def create(self, validated_data):
        # Check if the user is authenticated before creating the category
        if self.context['request'].user.is_authenticated:
            return Category.objects.create(**validated_data)
        else:
            raise serializers.ValidationError("User must be authenticated to create a category.")
    


    def update(self, instance, validated_data):
        # Check if the user is authenticated before updating the category
        if self.context['request'].user.is_authenticated:
            instance.category = validated_data.get('category', instance.category)
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("User must be authenticated to update a category.")

class ContentSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(max_length=120, read_only=True)
    permission_classes = [IsAuthenticated]
    category = serializers.CharField(max_length=120,write_only=True)
    class Meta:
        model = Content
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'created_by','category']

    def create(self, validated_data):
        # Check if the user is authenticated before creating the content
        if self.context['request'].user.is_authenticated:
            category=validated_data.get('category')
            validated_data['created_by'] = self.context['request'].user
            category_instance = Category.objects.filter(category=validated_data.get('category')).first()

            if category_instance:
                validated_data['category'] = category_instance
                content_instance = Content.objects.create(
                    title=validated_data.get('title'),
                    description = validated_data.get('description')
                )
                return content_instance
            else:
                raise serializers.ValidationError("category mismatched")

        else:
            raise serializers.ValidationError("User must be authenticated to create content.")
    

    def get_created_by(self, obj):
        if obj:
            return obj.created_by.user

    def update(self, instance, validated_data):
        # Check if the user is authenticated before updating the content
        if self.context['request'].user.is_authenticated:
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.category = validated_data.get('category', instance.category)
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("User must be authenticated to update content.")

