from django.conf.urls import url
from wpsblog.views.posts import list, detail


urlpatterns = [
        url(r'^', list, name='post-list'),
        url(r'(?P<post_id>\d+)/$', detail, name='post-detail'),
        ]
