from django.urls import path
from . import views

urlpatterns = [
    path('api/shows', views.ShowsList.as_view(), name='shows_list'),
    path('api/shows/<int:pk>', views.ShowsDetail.as_view(), name='shows_detail'),
    path('api/users', views.UsersList.as_view(), name='users_list'),
    path('api/users/<int:pk>', views.UsersDetail.as_view(), name='users_detail'),
]
