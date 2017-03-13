import requests 
import json

from django.template import loader
from django.shortcuts import render

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
