from django.shortcuts import render, redirect, reverse
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
                message=data["message"],
                bost_or_roast=data["boast"]
            )
            return redirect(reverse("home"))

    form = WritePost()
    return render(request, html, {'form': form})


def message_board_view(request):
    posts = Post.objects.order_by("-post_date")
    return render(request, "index.html", {'posts': posts})


def just_boast_view(request):
    posts = Post.objects.filter(bost_or_roast=True)
    return render(request, "index.html", {'posts': posts})


def just_roast_view(request):
    posts = Post.objects.filter(bost_or_roast=False)
    return render(request, "index.html", {'posts': posts})


def order_like_view(request):
    posts = Post.objects.order_by("-popularity")
    return render(request, "index.html", {'posts': posts})


def upvote(request, id):
    post = Post.objects.get(id=id)
    post.popularity += 1
    post.save()
    return redirect(reverse("home"))


def downvote(request, id):
    post = Post.objects.get(id=id)
    post.popularity -= 1
    post.save()
    return redirect(reverse("home"))