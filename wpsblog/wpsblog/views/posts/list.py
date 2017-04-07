from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from wpsblog.models import Post, Comment
from .base import PostBaseView


class PostListView(PostBaseView, ListView):

    template_name = "posts/list.html"
    context_object_name = "posts"
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get("per", 3)

#     def get_queryset(self):
#         queryset = super(PostListView, self).get_queryset()
#         page = self.request.GET.get("page", 1)
#         per = self.request.GET.get("per", 3)
# 
#         paginator = Paginator(queryset, per)
#         queryset = paginator.page(page)
# 
#         return queryset
# 
#     def get_context_data(self, **kwargs):
#         context = super(PostListView, self).get_context_data(**kwargs)
#         paginator = Paginator(context["posts"], 3)
#         context["posts"] = paginator.page(1)
# 
#         return context


#     def get_queryset(self):
#         queryset = super(PostListView, self).get_queryset()
#         return queryset.filter(is_public=True)
# 
# def list(request):
# 
#     page = request.GET.get("page", 1)
#     per = request.GET.get("per", 3)
# 
#     paginator = Paginator(Post.objects.public(), per)
#     
#     posts = paginator.page(page)
# #     p = Paginator(posts_list, 5)
# # 
# #     page = request.GET.get('page')
# # 
# #     try:
# #         posts = p.page(page)
# #     except PageNotAnInteger:
# #         posts = p.page(1)
# #     except EmptyPage:
# #         posts = p.page(p.num_pages)
# 
#     return render(
#            request,
#            "posts/list.html",
#            {
#             "posts": posts,
#             },
#     )
