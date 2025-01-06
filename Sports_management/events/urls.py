from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-player/', views.add_player, name='add_player'),
    path('add-event/', views.add_event, name='add_event'),
    path('schedule/', views.schedule, name='schedule'),
]
