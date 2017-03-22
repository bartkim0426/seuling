from django.shortcuts import redirect, render
from wpsblog.models import Post


def update(request, post_id):
    post = Post.objects.get(id=post_id)

    title = request.POST.get("title")
    content = request.POST.get('content')
#     post = Post.objects.get(id=post_id).update(
#             title=title,
#             content=content,
#             )
    post.title = title
    post.content = content

    post.save()
    
    return redirect(post)
