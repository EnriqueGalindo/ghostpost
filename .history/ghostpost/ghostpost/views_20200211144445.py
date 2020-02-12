from django.shortcuts import render
from .models import Post
from .forms import WritePost


def write_post_view(request, id):
    html = "genericForm.html"
    if request.method == "POST":
        form = WritePost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post = Post.objects.get(id=id)

    form = WritePost()
    return render(request, html, {{'form': form}})

messa
def ge_board_view(request):
    posts = Post.objects.all()
    return render(request, "index.html", {{'posts': posts}})
