from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=100,unique=True)
    team_logo =  models.ImageField(blank = True)
    team_state = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name

class Player(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    jersey_num = models.IntegerField()
    pic =  models.ImageField(blank = True)
    country = models.CharField(max_length=100)
    team = models.ForeignKey(Team,on_delete=models.CASCADE, related_name = "player")

    def __str__(self):
        return self.fname

class PlayerHistory(models.Model):
    matches = models.IntegerField(blank = True, null = True)
    run = models.IntegerField(blank = True, null = True)
    highest_score = models.IntegerField(blank = True, null = True)
    fifties = models.IntegerField(blank = True, null = True)
    hundreds = models.IntegerField(blank = True, null = True)
    player = models.ForeignKey(Player,on_delete=models.CASCADE,related_name ="Playerhistory")


class Match(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    winner = models.CharField(max_length=100)

    def __str__(self):
        return self.winner

class Points(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()

    def __str__(self):
        return self.team
