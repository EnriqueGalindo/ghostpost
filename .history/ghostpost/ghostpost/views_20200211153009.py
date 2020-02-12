from django.shortcuts import render, redirect
from .models import Post
from .forms import WritePost


def write_post_view(request):
    html = "genericForm.html"
    if request.method == "POST":
        form = WritePost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                screen_name=data["screen_name"],
                message=data["message"]
            )

    form = WritePost()
    return render(request, html, {'form': form})


def message_board_view(request):
    posts = Post.objects.all()
    return render(request, "index.html", {'posts': posts})


def upvote(request, id):
    post = Post.objects.get(id=id)
    post.popularity += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvote(request, id):
    post = Post.objects.get(id=id)
    post.popularity -= 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))