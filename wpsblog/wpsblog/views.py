import requests 
import json

from django.http import HttpResponse  
from django.template import loader
from django.shortcuts import render




def home(request): 
    template = loader.get_template("home.html")
    return render(
           request, 
           "home.html",
           {"site_name":"seul's blog"},
            )

#    return HttpResponse(
#            template.render(
#                {"site_name":"seul's blog"},
#                request,
#                )
#            )

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

    template = loader.get_template("news.html")
    if search:
        news_list = list(filter(
            lambda news: search in news.get('content'), 
            news_list,
            ))
    return render(
            request, 
            "news.html",
            {"news_list": news_list,}
            )


#    return HttpResponse(template.render(
#           {"news_list": news_list,},
#           request,
#           ))
