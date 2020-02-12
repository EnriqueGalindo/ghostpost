from django.db import models
from django.utils import timezone


class Post(models.Model):
    bost_or_roast = models.ForeignKey('Author', on_delete=models.CASCADE)
    screen_name = models.CharField(max_length=30)
    message = models.CharField(max_length=280)
    popularity = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class BoastOrRoast(models.IntegerChoices):
    Boast = 0, ('Boast')
    Roast = 1, ('Roast')

    def __str__(self):
        return self.title
