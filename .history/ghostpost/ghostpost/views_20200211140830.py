from django.shortcuts import render, redirect, reverse
from .models import Post
from .forms import PostAddForm
from django.http import HttpResponse


write