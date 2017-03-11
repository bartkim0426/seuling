import requests 
import json

from django.http import HttpResponse  

def home(request):
    return HttpResponse("hello world")

def room(request, room_id):
   # 방 번호 (room_id) 직방의 데이터를 그대로 보여주는 뷰 (컨트롤러)
    url = "https://api.zigbang.com/v1/items?detail=true&item_ids=" + room_id
    response = requests.get(url)
    return HttpResponse(
            response.content,
            content_type="application/json",
            )


def news(request):
#    from IPython import embed; embed()
    search =  request.GET.get('search') 

    url = "https://watcha.net/home/news.json?page=1&per=50"
    response = requests.get(url)
    
    news_dict = json.loads(response.content)
    news_list =  news_dict.get('news')

    form_html = """
    <form method="GET", action="/news/">
        <input type="text" name="search">
        <input type="submit" value="검색">

    </form>

    """

    if search:
        news_list = list(filter(
            lambda news: search in news.get('content'), 
            news_list,
            ))

    content = "<h1>NEWS by seul</h1>" +\
            "<p>this is my news page</p>" +\
            form_html +\
            "<p>{count}개의 영화 뉴스 정보가 있습니다.</p>".format(count= len(news_list)) +\
            "".join([
                "<p><h2>{title}</h2></p><img src={image} alt='movie_img'/> <p>{content}</p>".format(
                    title=news['title'], 
                    image=news['image'],
                    content=news['content'],)
                for news in news_list
                ])
    return HttpResponse(
           content
           )
