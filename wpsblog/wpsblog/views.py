import requests 
import json

from django.http import HttpResponse  
from django.conf import settings

def home(request):
    with open(settings.BASE_DIR + "/templates/home.html", "r") as template:
        content = template.read()
        site_name = "seulchan's blog"
        content = content.replace("## site_name ##", site_name)
    return HttpResponse(content)

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
    
    with open(settings.BASE_DIR+"/templates/news.html", "r") as template:
        content = template.read()

        count = len(news_list)
        news_content = "".join([
                    "<p><h2>{title}</h2></p><img src={image} alt='movie_img'/> <p>{content}</p>".format(
                        title=news['title'], 
                        image=news['image'],
                        content=news['content'],)
                    for news 
                    in news_list
                    ])
        content = content.replace("## count ##", str(count))
        content = content.replace("## news_content ##", news_content)
        return HttpResponse(content)
