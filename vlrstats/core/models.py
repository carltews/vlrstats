from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=20)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name="team1", on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name="team2", on_delete=models.CASCADE)
    date = models.DateTimeField()
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team1} vs {self.team2} ({self.date.date()})"