from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    players = models.ManyToManyField(Player, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Plan(models.Model):
   
    command = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
 
    def __str__(self):
        return self.command
    
class SportsSchedule(models.Model):
    SPORTS_CHOICES = [
        ('Football', 'Football'),
        ('Basketball', 'Basketball'),
        ('Tennis', 'Tennis'),
        ('Cricket', 'Cricket'),
    ]
    
    sports = models.CharField(max_length=50, choices=SPORTS_CHOICES)
    year = models.PositiveIntegerField()
    period_from = models.DateField()
    period_to = models.DateField()

    def __str__(self):
        return f"{self.sports} - {self.year}"