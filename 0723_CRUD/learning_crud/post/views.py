from django.shortcuts import render, redirect
from django.urls import reverse

from . import models


def main(request):

    return render(request, "post/main.html")


def post_list(request):
    all_posts = models.Post.objects.all()
    ctx = {
        "posts": all_posts,
    }
    return render(request, "post/post_list.html", ctx)


def post_detail(request, pk):

    post1 = models.Post.objects.get(pk=pk)
    ctx = {
        "post": post1,
    }

    return render(request, "post/post_detail.html", ctx)


def post_create(request):
    if request.method == "POST":

        new_Post = models.Post.objects.create(
            title=request.POST.get("tit"),
            writer=request.POST.get("wri"),
            content=request.POST.get("con"),
        )
        new_pk = new_Post.pk
        return redirect(reverse("post:post_d", kwargs={"pk": new_pk}))

    else:

        return render(request, "post/post_create.html")
