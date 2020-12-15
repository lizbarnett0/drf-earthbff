from django.db import models

# Create your models here.


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    slug = models.SlugField(blank=True)
    roll_out = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, related_name='questions', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.label


class Response(models.Model):
    question = models.ForeignKey(
        Question, related_name='responses', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    carbon_output = models.IntegerField(default=0)

    def __str__(self):
        return self.label


class Results(models.Model):
    carbon_output = models.IntegerField(default=0)
    owner = models.ForeignKey(
        'users.User', related_name='results', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
