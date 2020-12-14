from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100,  default='none')
    body = models.CharField(max_length=100, default='none')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}'s comment on {self.post}"
