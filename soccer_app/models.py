from django.db import models

# Create your models here.
class Player(models.Model):
	name = models.TextField()
	age = models.IntegerField()
	club = models.TextField() 
	position = models.TextField()
	home_location = models.TextField()
	years_played = models.IntegerField()