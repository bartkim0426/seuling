from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wpsblog.models import Post, Comment


def list(request):

    page = request.GET.get("page", 1)
    per = request.GET.get("per", 3)

    paginator = Paginator(Post.objects.public(), per)
    
    posts = paginator.page(page)
#     p = Paginator(posts_list, 5)
# 
#     page = request.GET.get('page')
# 
#     try:
#         posts = p.page(page)
#     except PageNotAnInteger:
#         posts = p.page(1)
#     except EmptyPage:
#         posts = p.page(p.num_pages)

    return render(
           request,
           "posts/list.html",
           {
            "posts": posts,
            },
    )
