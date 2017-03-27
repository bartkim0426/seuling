from django.conf.urls import url
from wpsblog.views.posts import list, detail, naver, create, new, edit, update, delete


urlpatterns = [
        url(r'^$', list, name='list'),
        url(r'^(?P<post_id>\d+)/$', detail, name='detail'),
        url(r'^naver/$', naver, name='naver'), 
        url(r'^create/$', create, name='create'), 
        url(r'^new/$', new, name='new'),
        url(r'^edit/(?P<post_id>\d+)/$', edit, name='edit'),
        url(r'^update/(?P<post_id>\d+)/$', update, name='update'),
        url(r'^delete/(?P<post_id>\d+)/$', delete, name='delete'),
        ]
