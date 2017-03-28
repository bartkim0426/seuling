from django.conf.urls import url
from wpsblog.views.posts import list, detail, naver, create, new, edit, update, delete, create_comment, new_comment


urlpatterns = [
        url(r'^$', list, name='list'),
        url(r'^(?P<post_id>\d+)/$', detail, name='detail'),
        url(r'^naver/$', naver, name='naver'), 
        url(r'^create/$', create, name='create'), 
        url(r'^new/$', new, name='new'),
        url(r'^(?P<post_id>\d+)/edit/$', edit, name='edit'),
        url(r'^(?P<post_id>\d+)/update/$', update, name='update'),
        url(r'^(?P<post_id>\d+)/delete/$', delete, name='delete'),

        url(r'^(?P<post_id>\d+)/new_comment/$', new_comment, name='new-comment'),
        url(r'^(?P<post_id>\d+)/create_comment/$', create_comment, name='create-comment'), 
        ]
