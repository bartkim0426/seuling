from django.contrib import admin

from wpsblog.models import Post, Comment, Naverpost, Crawlnaver


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Naverpost)
admin.site.register(Crawlnaver)
