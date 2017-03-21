from django.core.management.base import BaseCommand, CommandError
from wpsblog.models import Naverpost as naver
import requests
from bs4 import BeautifulSoup

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('query', type=str)

    def handle(self, *args, **options):
        query = options.get('query')
        url = "https://search.naver.com/search.naver?where=post&sm=tab_jum&ie=utf8&query=" + query
        
        response = requests.get(url)
        r = BeautifulSoup(response.content, "html.parser")
        
        posts_list = r.find_all('li', class_='sh_blog_top')

        for post in posts_list: 
            post = posts_list[0]
            post_image = post.select_one('div a img').get('src')   
            post_title = post.select_one('dt a').get('title')
            post_content = post.select_one('dd.sh_blog_passage').get_text()
            post_url = post.select_one('dt a').get('href')
            q = naver.objects.create(title=post_title, imageadress=post_image, content=post_content, urladdress=post_url)
            q.save()

        self.stdout.write("Naver에서 {query} 블로그 포스트를 크롤링합니다.".format(query=query))

