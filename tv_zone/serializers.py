from rest_framework import serializers
from .models import Shows
from .models import Users

class ShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
        fields = ('id', 'title', 'description', 'cast', 'genre', 'avg_rating', 'year', 'video', 'added_by', 'user_ratings', 'user_reviews')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'password', 'reviews')
