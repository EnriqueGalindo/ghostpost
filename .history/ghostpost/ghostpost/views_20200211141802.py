from django.shortcuts import render, redirect, reverse
from .models import Post
from .forms import PostAddForm
from django.http import HttpResponse


def write_post_view(requst, id):
    