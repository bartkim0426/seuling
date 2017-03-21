from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=120,
    )
    content = models.TextField()
    
    def __str__(self):
        return self.title

    def get_url(self):
        url = "/posts/" + str(self.id)  + "/"
        return url
