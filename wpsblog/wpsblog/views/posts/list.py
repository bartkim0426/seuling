from django.shortcuts import render

from wpsblog.models import Post, Comment

def list(request):
    return render(
           request,
           "posts/list.html",
           {
            "posts": Post.objects.public(),
            },
    )
