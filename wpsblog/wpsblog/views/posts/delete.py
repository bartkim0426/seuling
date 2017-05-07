from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from wpsblog.models import Post


def delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()

    return redirect(
            reverse(
                "posts:list",
                )
            )

