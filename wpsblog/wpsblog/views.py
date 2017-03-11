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

    content = "<h1>NEWS by seul</h1>" +\
            "<p>this is my news page</p>" +\
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

           
           
#def news(request):
#    search = request.GET.get('search') # title에 search가 포함되어있는가?
#
#    response = requests.get("https://watcha.net/home/news.json?page=1&per=50")
#   #  from IPython import embed; embed()
#    news_dict = json.loads(response.content) # news_dict =  response.json()
#    
#    news_items_list = news_dict.get("news")
#    if search:
#            news_items_list = list(filter(
#                lambda news: search in news.get('content'),
#                news_items_list, 
#                ))
#    else: 
#        search = ""
#    
#    content = "<h1>News</h1>" +\
#              "<p>This is new page. </p>" +\
#              "<p>{count}개의 검색 결과가 있습니다</p>".format(count=len(news_items_list)) +\
#              "".join([
#                "<h2>{title}</h2><img src={image_src} alt='news_image' /><p>{content}</p>".format(
#                title = news.get('title'),
#                image_src = news.get('image'),
#                content = news.get('content'),
#                      ) 
#                # +\
#                #              "<p>search {search}:{news_search}</p>".format(news_search=
#                #  [x for x in news.get('content').split(" ")
#                #      if search in x], 
#                #  search = search
#                #  )
#                  for news
#                  in news_items_list
#                  if search in news.get('content')
#                  ])
#
#    return HttpResponse(
#            content,
#            # content_type="application/json",
#            )
