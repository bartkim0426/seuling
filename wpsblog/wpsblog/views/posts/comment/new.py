from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from wpsblog.models import Post


@login_required
def new_comment(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(
           request,
           "posts/new_comment.html",
           {"post": post},
           )
