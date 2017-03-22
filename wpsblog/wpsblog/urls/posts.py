from django.conf.urls import url
from wpsblog.views.posts import list, detail, naver, create, new 


urlpatterns = [
        url(r'^$', list, name='post-list'),
        url(r'^(?P<post_id>\d+)/$', detail, name='post-detail'),
        url(r'^naver/$', naver, name='post-naver'), 
        url(r'^create/$', create, name='post-create'), 
        url(r'^new/$', new, name='post-new'),
        ]
