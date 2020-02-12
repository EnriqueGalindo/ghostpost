from django import forms


class PostAddForm(forms.Form):
    screen_name = forms.CharField(max_length=30)
    message = models.CharField(max_length=280)
    popularity = models.IntegerField()
    post_date = models.DateTimeField(auto_now_add=True)