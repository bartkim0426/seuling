from django.shortcuts import render
from wpsblog.models import Post


def edit(request, pk):
    post = Post.objects.get(id=pk)

    return render(
           request,
           "posts/edit.html",
           {"post": post},
           )
