from django.conf.urls import url
from wpsblog.views.posts import PostListView, PostDetailView, naver, PostCreateView, new, edit, update, delete, CommentCreateView, new_comment, edit_comment, update_comment, delete_comment


urlpatterns = [
        url(r'^$', PostListView.as_view(), name='list'),
        url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
        url(r'^naver/$', naver, name='naver'), 
        url(r'^create/$', PostCreateView.as_view(), name='create'), 
        url(r'^new/$', new, name='new'),
        url(r'^(?P<pk>\d+)/edit/$', edit, name='edit'),
        url(r'^(?P<pk>\d+)/update/$', update, name='update'),
        url(r'^(?P<pk>\d+)/delete/$', delete, name='delete'),

        # comment
        url(r'^(?P<pk>\d+)/new_comment/$', new_comment, name='new-comment'),
        url(r'^(?P<pk>\d+)/create_comment/$', CommentCreateView.as_view(), name='create-comment'), 
        url(r'^(?P<pk>\d+)/edit_comment/(?P<comment_id>\d+)/$', edit_comment, name='edit-comment'),
        url(r'^(?P<pk>\d+)/update_comment/(?P<comment_id>\d+)/$', update_comment, name='update-comment'),
        url(r'^(?P<pk>\d+)/delete_comment/(?P<comment_id>\d+)/$', delete_comment, name='delete-comment'),
        ]
