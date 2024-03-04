from django.db import models
from django.conf import settings


# This class stores users Actions.
class Action(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Links it with the user

    name = models.CharField(max_length=50) # the name of the action
    date_created = models.DateTimeField(auto_now_add=True) # The time that the activity was created

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['user'] 

class ActionTime(models.Model):
    action = models.ForeignKey(Action, on_delete=models.CASCADE) # Links it with the action
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField(null = True, blank = True)
    is_active = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.action.name} recorded from {self.start_time} to {self.stop_time}"
    
    class Meta:
        ordering = ['start_time'] # This ensures thay when you query for 'ActionTime' objetcs, they are ordered by the start_time field.


