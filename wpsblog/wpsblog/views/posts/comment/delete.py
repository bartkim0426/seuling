from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from wpsblog.models import Post


def delete_comment(request, pk, comment_id):

    post = Post.objects.get(id=pk)
    
    comment = post.comment_set.get(id=comment_id)

    comment.delete()

    return redirect(post)

