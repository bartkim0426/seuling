import requests 
import json

from django.http import HttpResponse  
from wpsblog.renderer import render

def home(request):
    return render("home", {"site_name":"seul's blog"})

def room(request, room_id):
   # 방 번호 (room_id) 직방의 데이터를 그대로 보여주는 뷰 (컨트롤러)
    url = "https://api.zigbang.com/v1/items?detail=true&item_ids=" + room_id
    response = requests.get(url)
    return HttpResponse(
            response.content,
            content_type="application/json",
            )


def news(request):

    search =  request.GET.get('search') 

    url = "https://watcha.net/home/news.json?page=1&per=50"
    response = requests.get(url)
    
    news_dict = json.loads(response.content)
    news_list =  news_dict.get('news')

    if search:
        news_list = list(filter(
            lambda news: search in news.get('content'), 
            news_list,
            ))
    count = len(news_list)
    news_content = "".join([
        "<h2>{title}</h2><img src={img_src} alt='movie_image'/><p>{content}</p>".format(
            title = news.get('title'),
            img_src = news.get('image'),
            content = news.get('content'),
            )
        for news
        in news_list
        ])
    return render("news", {
        "count": str(count),
        "news_content": news_content
        }) 
