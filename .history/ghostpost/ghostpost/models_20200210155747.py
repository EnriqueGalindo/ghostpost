from django.db import models


class Post(models.Model):
    screen_name = models.CharField(max_length=30)
    