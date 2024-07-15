from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    """
    Model representing an event.

    Attributes:
    name (str): The name of the event.
    date (DateField): The date of the event.
    location (str): The location of the event.
    description (str): A detailed description of the event.
    """ 
    name = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """
        Return a string representation of the event, which is its name.
        """
        return self.name
    
class Participation(models.Model):
    """
    Model representing a user's participation in an event.

    Attributes:
    event: The event the user is participating in.
    user: The user who is participating in the event.
    """ 
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a string representation of the participation, which includes the user's username and the event's name.
        """
        return f"{self.user.username} - {self.event.name}"





