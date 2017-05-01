from django.shortcuts import render
from wpsblog.models import Post


def edit_comment(request, pk, comment_id):
    post = Post.objects.get(id=pk)
    comment = post.comment_set.get(id=comment_id)

    return render(
           request,
           "posts/edit_comment.html",
           {
            "post": post,
            "comment": comment,
            }
           )
