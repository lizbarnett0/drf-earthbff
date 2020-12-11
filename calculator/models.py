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

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.label


class Response(models.Model):
    question = models.ForeignKey(Question, related_name='responses', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    carbon_output = models.IntegerField(default=0)

    def __str__(self):
        return self.label


class QuizTaker(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    carbon_footprint = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    date_finished = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email


class UsersResponse(models.Model):
    quiz_taker = models.ForeignKey(QuizTaker, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.label
