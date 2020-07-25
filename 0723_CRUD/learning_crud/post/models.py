from django.db import models

# class PostList(models.Model):


class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)
    writer = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

