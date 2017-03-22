from django.shortcuts import render

from wpsblog.models import Crawlnaver


def naver_posts_list(request):
    keyword = request.GET.get('keyword')
    naver_posts = Crawlnaver.objects.all()
    
    if keyword:
        naver_posts = naver_posts.filter(keyword=keyword)
#     if keyword:
#         naver_posts = [
#                 naver_post
#                 for naver_post
#                 in naver_posts
#                 if naver_post.keyword == keyword
#                 ]

    return render(
           request,
           "naver_posts/list.html",
           {
               "naver_posts": naver_posts,
               "keyword": keyword,
            },
    )
