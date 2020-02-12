from django.db import models
from django.utils import timezone

class Post(models.Model):
    screen_name = models.CharField(max_length=30)
    message = models.CharField(max_length=280)
    popularity = models.IntegerField()
    post_date = models.DateTimeField(default=timezone.now, read)

    def __str__(self):
        return self.title
