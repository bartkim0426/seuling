from django.conf.urls import url
from django.contrib import admin
from wpsblog.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
    url(r'^news/$', news, name="news"),
    url(r'^about/us/$', about, name="about"),
    url(r'^policy/terms/$', terms, name="terms"),
    url(r'^policy/privacy/$', privacy, name="privacy"),
    url(r'^policy/disclaimer/$', disclaimer, name='disclaimer'),
    
]


# 1. about page (.../about , .../about/us , .../about-us/)

# 2. 정책
# 이용약관 page ( /terms/ )
# 개인정보 취급방침 페이지 (... /privacy/)
# 법적 고지와 책임의 한계 (... /disclaimer/)

# 이것들을 header에 넣어서 동작하게

