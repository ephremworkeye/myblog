from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(null=True)
    author = models.ForeignKey(User, related_name='blog_post', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        

