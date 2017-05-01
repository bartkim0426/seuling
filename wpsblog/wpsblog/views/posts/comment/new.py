from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from wpsblog.models import Post


@login_required
def new_comment(request, pk):
    post = Post.objects.get(id=pk)

    return render(
           request,
           "posts/new_comment.html",
           {"post": post},
           )
