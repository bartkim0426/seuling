from django.views.generic import View
from django.views.generic.edit import CreateView

from django.shortcuts import redirect, render

from wpsblog.models import Comment, Post


class CommentBaseView(View):
    model = Comment


class CommentCreateView(CommentBaseView, CreateView):
    fields = [
        'content',        
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs.get('pk'))

        return super(CommentCreateView, self).form_valid(form)

# def create_comment(request, pk):
# 
#     user = request.user
# 
#     content = request.POST.get("content")
# 
#     post = Post.objects.get(id=pk)
# 
#     comment = post.comment_set.create(
#             content = content,
#             user = user
#             )
# 
#     # user 관점
# #     comment = user.comment_set.create(
# #             post=post,
# #             content=content,
# #             )
# 
#     return redirect(comment)
