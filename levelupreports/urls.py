from levelupreports.views.users.eventsbyuser import userevent_list
from django.urls import path
from .views import usergame_list

urlpatterns = [
    path('reports/usergames', usergame_list),
    path('reports/userevents', userevent_list)
]
