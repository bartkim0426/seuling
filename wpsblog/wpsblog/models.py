from django.db import models

class Post(models.Model):
    title = models.CharField(
        max_length=120,
    )
    content = models.TextField()
    
    def __str__(self):
        return self.title
# from django.db.models import Model
# from django.db.models import CharField, TextField
# 
# class Post(Model):
# 
#     title = CharField(
#         max_length=120,
#     )
#     
#     content = TextField()
