from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Like(models.Model):

    username = models.CharField(max_length=32)

    def __str__(self):
        return self.username


class Post(models.Model):

    user = models.ForeignKey(User)
    title = models.CharField(max_length=32)
    body = models.TextField()
    likes = models.ManyToManyField(Like, related_name='user_likes')
    like = models.IntegerField(default=0)
    tags = TaggableManager()
    image = models.ImageField(upload_to="img", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-created']

