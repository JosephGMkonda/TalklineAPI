from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from posts.models import Post


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
    posts = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    content  = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ['-timestamp']


    def __unicode__(self):  
        return str(self.user.username)

    def __str__(self):
        return str(self.user.username)

    
