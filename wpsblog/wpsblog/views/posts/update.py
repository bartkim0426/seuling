from django.shortcuts import redirect, render
from wpsblog.models import Post


def update(request, pk):
    title = request.POST.get("title")
    content = request.POST.get('content')
    
    post = Post.objects.get(id=pk)
    
    post.title = title
    post.content = content
    post.save()

    return redirect(post)
