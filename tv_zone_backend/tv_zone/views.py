# from django.shortcuts import render
from rest_framework import generics
from .serializers import ShowsSerializer
from .models import Shows
from .serializers import UsersSerializer
from .models import Users
# Create your views here.

class ShowsList(generics.ListCreateAPIView):
    queryset = Shows.objects.all().order_by('id')
    serializer_class = ShowsSerializer

class ShowsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shows.objects.all().order_by('id')
    serializer_class = ShowsSerializer

class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all().order_by('id')
    serializer_class = UsersSerializer

class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all().order_by('id')
    serializer_class = UsersSerializer
