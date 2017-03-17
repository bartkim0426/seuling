from django.conf.urls import url
from wpsblog.views.policy import privacy, terms, disclaimer


urlpatterns = [
        url(r'^terms/$', terms, name="terms"),
        url(r'^privacy/$', privacy, name="privacy"),
        url(r'^disclaimer/$', disclaimer, name='disclaimer'),
        ]
