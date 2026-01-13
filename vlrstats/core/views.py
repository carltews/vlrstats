from django.shortcuts import render
from .models import Player, Team, Match

def home(request):
    return render(request, "home.html")

def players(request):
    players = Player.objects.all()
    return render(request, "players.html", {"players": players})

def teams(request):
    teams = Team.objects.all()
    return render(request, "teams.html", {"teams": teams})

def matches(request):
    matches = Match.objects.all()
    return render(request, "matches.html", {"matches": matches})

def stats(request):
    players = Player.objects.all().order_by("-rating")
    return render(request, "stats.html", {"players": players})