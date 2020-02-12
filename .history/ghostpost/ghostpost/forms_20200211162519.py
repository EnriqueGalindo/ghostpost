from django import forms


class WritePost(forms.Form):
    screen_name = forms.CharField(max_length=30)
    message = forms.CharField(max_length=280)
    Boast = form
