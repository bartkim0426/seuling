from django.conf.urls import url
from wpsblog.views.posts import list, detail, naver, create, new, edit, update


urlpatterns = [
        url(r'^$', list, name='post-list'),
        url(r'^(?P<post_id>\d+)/$', detail, name='post-detail'),
        url(r'^naver/$', naver, name='post-naver'), 
        url(r'^create/$', create, name='post-create'), 
        url(r'^new/$', new, name='post-new'),
        url(r'^(?P<post_id>\d+)/edit/$', edit, name='post-edit'),
        url(r'^(?P<post_id>\d+)/update/$', update, name='post-update'),
        ]
