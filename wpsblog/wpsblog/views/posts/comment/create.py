from django.shortcuts import redirect, render
from wpsblog.models import Post


def create_comment(request, post_id):
    content = request.POST.get("content")

    post = Post.objects.get(id=post_id)

    post.comment_set.create(
            content = content,
            )

    return redirect(comment)
