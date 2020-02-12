from django.db import models
from datetime import datetime


class Post(models.Model):
    screen_name = models.CharField(max_length=30)
    message = models.CharField(max_length=280)
    popularity = models.IntegerField()
    post_date = models.DateTimeField(default=timezone.now, readonly=True)

    def __str__(self):
        return self.title