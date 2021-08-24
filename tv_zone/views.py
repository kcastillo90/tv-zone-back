# from django.shortcuts import render
from rest_framework import generics
from .serializers import ShowsSerializer
from .models import Shows
from .serializers import UsersSerializer
from .models import Users

# checks and creates passwords
from django.contrib.auth.hashers import make_password, check_password
# allows you to send json as a response
from django.http import JsonResponse
# allows you to translate dictionaries into JSON data
import json

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

# function that performs auth
def check_login(request):
    # if a get request is made, return an empty {}
    if request.method == 'GET':
        return JsonResponse({})

    # check if a put request is made
    if request.method == 'PUT':

        jsonRequest = json.loads(request.body) # makee the request json format
        username = jsonRequest['username'] # gets user from the request
        password = jsonRequest['password'] # gets password from the request
        if Users.objects.get(username=username): # see if user exists in db
            user = Users.objects.get(username=username) # find user object with matching user
            if check_password(password, user.password):  # checks if password matches
                return JsonResponse({'id': user.id, 'username': user.username}) # if passwords match, return a user dictionary
            else: # returns empty object if passwords don't match
                return JsonResponse({})
        else: # if user doesn't exist in db, return empty dictionary
            return JsonResponse({})

























#
