from django.conf.urls import url
from wpsblog.views.auth import login, signup


urlpatterns = [
        url(r'^login/$', login, name='login'),
        url(r'^signup/$', signup, name='signup'),
        ]
