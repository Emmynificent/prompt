# from sqlite3 import Time
from django.db import models
from datetime import datetime, time
# Create your models here.
class Prompt(models.Model):
    title = models.CharField(max_length= 150, blank=True)
    description = models.TextField(max_length=500, blank=True)
    # created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    