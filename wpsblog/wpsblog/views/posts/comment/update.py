from django.shortcuts import redirect, render
from wpsblog.models import Post


def update_comment(request, post_id, comment_id):
    content = request.POST.get("content")

    post = Post.objects.get(id=post_id)
    comment = post.comment_set.get(id=comment_id)

    comment.content = content
    comment.save()

    return redirect(comment)
