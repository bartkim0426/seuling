from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User


class PostManager(models.Manager):

    def public(self):
        return self.filter(is_public=True)


class Post(models.Model):

    user = models.ForeignKey(User)

    objects = PostManager()

    title = models.CharField(
        max_length=120,
    )
    content = models.TextField()
    image = models.ImageField(
            blank=True,
            null=True,
            )
    is_public = models.BooleanField(
            default=True
            )
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
                'posts:detail',
            kwargs = { 'pk': self.id },
                )

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return "http://placehold.it/300x200"
