from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'users.User', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
