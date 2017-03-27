from django.conf.urls import url
from wpsblog.views.posts import list, detail, naver


urlpatterns = [
        url(r'^$', list, name='list'),
        url(r'^(?P<post_id>\d+)/$', detail, name='detail'),
        url(r'^naver/$', naver, name='naver'), 
        ]
