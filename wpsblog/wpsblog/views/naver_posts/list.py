from django.shortcuts import render

from wpsblog.models import Crawlnaver


def naver_posts_list(request):
    return render(
           request,
           "naver_posts/list.html",
           {
               "naver_posts": Crawlnaver.objects.all(),
            },
    )
