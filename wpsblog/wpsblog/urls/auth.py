from django.conf.urls import url
from wpsblog.views.auth import LoginView, SignupView, LogoutView, MyPageView 


urlpatterns = [
        url(r'^login/$', LoginView.as_view(), name='login'),
        url(r'^signup/$', SignupView.as_view(), name='signup'),
        url(r'^logout/$', LogoutView.as_view(), name='logout'),
        url(r'^my/page/$', MyPageView.as_view(), name="mypage"),
        ]
