from django import forms
from django.utils import timezone


class WritePost(forms.Form):
    screen_name = forms.CharField(max_length=30)
    message = forms.CharField(max_length=280)
    popularity = forms.IntegerField()
    