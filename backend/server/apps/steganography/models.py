from django.db import models

# Create your models here.


class StatusTracker(models.Model):
    created = models.DateTimeField(auto_now=True)
    progress = models.IntegerField(default=0)