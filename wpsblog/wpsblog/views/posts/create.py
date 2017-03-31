from django.shortcuts import redirect, render
from wpsblog.models import Post


def create(request):
    title = request.POST.get("title")
    content = request.POST.get('content')
    image = request.FILES.get("image")

    post = Post.objects.create(
            title=title,
            content=content,
            image=image,
            )
    return redirect(post)
