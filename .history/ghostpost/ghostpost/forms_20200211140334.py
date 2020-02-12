from django import forms


class PostAddForm(forms.Form):
    screen_name = forms.CharField(max_length=30)
    message = forms.CharField(max_length=280)
    popularity = forms.IntegerField()
    post_date = forms.DateTimeField(auto_now_add=True)