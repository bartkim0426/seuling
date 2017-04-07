from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .base import PostBaseView
from wpsblog.models import Post


class PostDetailView(PostBaseView, DetailView):
    
    template_name = "posts/detail.html"

#     def get_object(self):
#         object = get_object_or_404(Post, id=self.kwargs.get("post_id"))
#         return object
# 
#     def get_context_data(self, **kwargs):
#         context = super(PostDetailView, self).get_context_data(**kwargs)
#         context["post"] = Post.objects.filter(pk=self.kwargs.get("pk"))
#         return context
# # def detail(request, post_id):
#     post = Post.objects.get(id=post_id)
#     
#     return render(
#            request,
#            "posts/detail.html",
#            {"post": post},
#            )
