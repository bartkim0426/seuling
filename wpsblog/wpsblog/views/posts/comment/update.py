from django.shortcuts import redirect, render
from wpsblog.models import Post


def update_comment(request, pk, comment_id):
    content = request.POST.get("content")

    post = Post.objects.get(id=pk)
    comment = post.comment_set.get(id=comment_id)

    comment.content = content
    comment.save()

    return redirect(comment)
