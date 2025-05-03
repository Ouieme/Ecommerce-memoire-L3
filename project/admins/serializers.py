from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Admin
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class ProfileAdminSerializer(serializers.ModelSerializer):
    nom = serializers.CharField(required=False)
    type_Admin = serializers.CharField(required=False)
    image =serializers.ImageField(required=False)
    user = UserSerializer()

    class Meta:
        model = Admin
        fields = ['id', 'user', 'nom', 'type_Admin','image']

    def get_user(self, obj):
        return obj.user.username
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        admin = Admin.objects.create(user=user, **validated_data)
        return admin
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_serializer = self.fields['user']
            user_instance = instance.user
            user = user_serializer.update(user_instance, user_data)
            validated_data['user'] = user
        return super().update(instance, validated_data)    


class AdminSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Admin
        fields = ['id','username', 'type_Admin','image']

