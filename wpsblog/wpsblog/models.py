from django.db import models
from django.core.urlresolvers import reverse
from django.shortcuts import render


class Post(models.Model):
    title = models.CharField(
        max_length=120,
    )
    content = models.TextField()

    def get_absolute_url(self):
        return reverse(
                'posts:detail',
            kwargs = { 'post_id': self.id },
                )


class Naverpost(models.Model):
    title = models.CharField(
        max_length=120,
    )
    content = models.TextField()
    
    urladdress = models.CharField(
                  max_length=120,
                  null=True,
                  blank=True,
    )
    imageadress = models.CharField(
                  max_length=120,
                  null=True,
                  blank=True,
    )

    def __str__(self):
        return self.title

class Crawlnaver(models.Model):
    keyword = models.CharField(
            max_length=16
            )
    title = models.CharField(
            max_length=256
    )
    content = models.TextField()
    original_url = models.URLField()
    thumbnail_image_element= models.URLField()

    def __str__(self):
        return self.title
