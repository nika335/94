from django.db import models

class Events(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title