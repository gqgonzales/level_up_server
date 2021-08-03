# The last step is to establish some URL routes that any client application can use to register and login a gamer to use the API.

from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user

urlpatterns = [
    # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    # Requests to http://localhost:8000/login will be routed to the login_user function
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
