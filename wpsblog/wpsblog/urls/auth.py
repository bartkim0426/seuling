from django.conf.urls import url
from wpsblog.views.auth import login, signup, logout, mypage


urlpatterns = [
        url(r'^login/$', login, name='login'),
        url(r'^signup/$', signup, name='signup'),
        url(r'^logout/$', logout, name='logout'),
        url(r'^my/page/$', mypage, name="mypage"),
        ]
