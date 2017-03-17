# from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from wpsblog.views import home, news, room, about, policy


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
    url(r'^news/$', news, name="news"),
    url(r'^about/us/$', about, name="about"),
    url(r'^policy/', include("wpsblog.urls.policy", namespace='policy')),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#             url(r'^__debug__/', include(debug_toolbar.urls)),
#             ] + urlpatterns
