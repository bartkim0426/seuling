from django.db import models


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
