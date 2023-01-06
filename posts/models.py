from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.urls import reverse
from django.utils.safestring import mark_safe

import uuid

from comments.models import Comment

class PostManager(models.Manager):
    def active(self,*args, **kwargs):
        return super(PostManager,self).filter(draft=False).filter(publish__lte=timezone.now)

def upload_location(instance, filename):
    PostModel = instance.__class__
    obj_exist = PostModel.objects.order_by("id").last()
    new_id = 1

    if obj_exist:
        new_id = obj_exist.id + 1


    return "%s/%s" %(new_id,filename)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    content = models.TextField()
    picture = models.ImageField(upload_to=upload_location,null=True,blank=True)
    published= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = PostManager()

    def __unicode__(self):
        return self.content
    def __str__(self):
        return self.content
    class Meta:
        ordering = ['-published','-updated']

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    def get_api_url(self):
        return reverse("posts-api:detail", kwargs={"slug": self.slug})

    @property
    def get_content_type(self):
        instance = self
        content_type= ContentType.objects.get_for_model(instance.__class__)
        return content_type
    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

def create_slug(instance, new_slug=None):
    slug = slugify(instance.content)

    if new_slug is not None:
        slug = new_slug

        qs = Post.objects.filter(slug=slug).order_by('-id')
        exits = qs.exists()

        if exits:
            new_slug = "%s-%s" %(slug, qs.first().id)
        return slug
