from django.shortcuts import redirect, render
from wpsblog.models import Post


def create(request):
    if reqeust.method == "POST":

        title = request.POST.get("title")
        content = request.POST.get('content')

        post = Post.objects.create(
                title=title,
                content=content,
                )

    return redirect(post)
