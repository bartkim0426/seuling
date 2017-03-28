from django.shortcuts import render
from wpsblog.models import Post


def new(request):
    return render(
           request,
           "posts/new.html",
           {},
           )
