from rest_framework import serializers
from .models import Shows
from .models import Users

from django.contrib.auth.hashers import make_password, check_password # allows creation and checking of passwords

class ShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
        fields = ('id', 'title', 'description', 'cast', 'genre', 'avg_rating', 'year', 'video', 'added_by', 'user_ratings', 'user_reviews')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'password')

    # Hashes new password on account creation
    def create(self, validated_data):
        user = Users.objects.create(
        username = validated_data['username'],
        password = make_password(validated_data['password'])
        )
        user.save()
        return user

    # Hashes any updated passwords
    def update(self, instance, validated_data):
        user = Users.objects.get(username=validated_data['username'])
        user.password = make_password(validated_data["password"])
        user.save()
        return user
