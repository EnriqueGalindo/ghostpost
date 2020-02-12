from django.shortcuts import render, redirect, reverse
from .models import Post
from .forms import PostAddForm
from django.http import HttpResponse


def write_post_view(request, id):
    post = Post.objects.get(id=id)
    return render(request, html, {{'form':form}})


