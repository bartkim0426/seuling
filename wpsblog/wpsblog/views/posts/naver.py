from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from IPython import embed;
from wpsblog.models import Naverpost


def naver(request):
#     url = "https://search.naver.com/search.naver?where=post&sm=tab_jum&ie=utf8&query=파이썬"
#     response = requests.get(url)
#     r = BeautifulSoup(response.content, "html.parser")
#     posts_list = r.find_all('li', class_='sh_blog_top')
#     post = posts_list[0] 
#     post_image = post.select_one('div a img').get('src')   
#     post_title = post.select_one('dt a').get('title')
#     post_content = post.select_one('dd.sh_blog_passage').get_text()
#     post_url = post.select_one('dt a').get('href')

    return render(
           request,
           "posts/naver.html",
           {"naverpost": Naverpost.objects.all()}, 
           )
