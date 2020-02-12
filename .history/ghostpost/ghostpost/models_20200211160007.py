from django.db import models
from django.utils import timezone


class Post(models.Model):
    screen_name = models.CharField(max_length=30)
    message = models.CharField(max_length=280)
    popularity = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Answer(models.IntegerChoices):
    NO = 0, _('No')
    YES = 1, _('Yes')

    def __str__(self):
        return self.title
