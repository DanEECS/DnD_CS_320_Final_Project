from django.db import models


class Character(models.Model):
    characterName = models.CharField(max_length=100)
    playerName = models.CharField(max_length=100)
    Class = models.TextField()
    race = models.TextField()
    background = models.TextField()
    level = models.IntegerField()
    alignment = models.TextField()
    experience = models.IntegerField()


# Create your models here.
