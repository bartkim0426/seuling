from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from wpsblog.models import Post, Comment


class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        return queryset.filter(is_public=True)

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
