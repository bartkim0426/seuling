from django.conf.urls import url
from wpsblog.views.posts import PostListView, PostDetailView, naver, create, new, edit, update, delete, create_comment, new_comment, edit_comment, update_comment, delete_comment


urlpatterns = [
        url(r'^$', PostListView.as_view(), name='list'),
        url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
        url(r'^naver/$', naver, name='naver'), 
        url(r'^create/$', create, name='create'), 
        url(r'^new/$', new, name='new'),
        url(r'^(?P<post_id>\d+)/edit/$', edit, name='edit'),
        url(r'^(?P<post_id>\d+)/update/$', update, name='update'),
        url(r'^(?P<post_id>\d+)/delete/$', delete, name='delete'),

        # comment
        url(r'^(?P<post_id>\d+)/new_comment/$', new_comment, name='new-comment'),
        url(r'^(?P<post_id>\d+)/create_comment/$', create_comment, name='create-comment'), 
        url(r'^(?P<post_id>\d+)/edit_comment/(?P<comment_id>\d+)/$', edit_comment, name='edit-comment'),
        url(r'^(?P<post_id>\d+)/update_comment/(?P<comment_id>\d+)/$', update_comment, name='update-comment'),
        url(r'^(?P<post_id>\d+)/delete_comment/(?P<comment_id>\d+)/$', delete_comment, name='delete-comment'),
        ]
