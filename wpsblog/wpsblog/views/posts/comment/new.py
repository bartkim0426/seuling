from django.shortcuts import render
from wpsblog.models import Post


def new_comment(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(
           request,
           "posts/new_comment.html",
           {"post": post},
           )
