from django.shortcuts import redirect, render
from wpsblog.models import Post


def create_comment(request, post_id):

    user = request.user

    content = request.POST.get("content")

    post = Post.objects.get(id=post_id)

    comment = post.comment_set.create(
            content = content,
            user = user
            )

    # user 관점
#     comment = user.comment_set.create(
#             post=post,
#             content=content,
#             )

    return redirect(comment)
