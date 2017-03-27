from django.db import models
from django.urls.base import reverse
from django.shortcuts import render


class Post(models.Model):
    title = models.CharField(
        max_length=120,
    )
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
                'posts:detail',
            kwargs = { 'post_id': self.id },
                )
