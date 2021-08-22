from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/shows', views.ShowsList.as_view(), name='shows_list'),
    path('api/shows/<int:pk>', views.ShowsDetail.as_view(), name='shows_detail'),
    path('api/users', views.UsersList.as_view(), name='users_list'),
    path('api/users/<int:pk>', views.UsersDetail.as_view(), name='users_detail'),
    path('api/users/login', csrf_exempt(views.check_login), name="check_login") #routes api/users/login to check_login function for auth
]
