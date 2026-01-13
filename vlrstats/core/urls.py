from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("players/", views.players, name="players"),
    path("teams/", views.teams, name="teams"),
    path("matches/", views.matches, name="matches"),
    path("stats/", views.stats, name="stats"),
]