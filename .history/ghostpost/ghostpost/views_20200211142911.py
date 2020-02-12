from django.shortcuts import render, redirect, reverse
from .models import Post
from .forms import PostAddForm
from django.http import HttpResponse


def write_post_view(request, id):
    html = "genericForm.html"
    form = writePost(request.P)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post = Post.objects.get(id=id)
    return render(request, html, {{'form':form}})

def message_board_view(request):

