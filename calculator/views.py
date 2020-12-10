from django.shortcuts import render
from rest_framework import viewsets
from .models import Quiz, Question, Response, QuizTaker, UsersResponse
from .serializers import QuizSerializer, QuestionSerializer, ResponseSerializer, QuizTakerSerializer, UsersResponseSerializer

# Create your views here.


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer


class QuizTakerViewSet(viewsets.ModelViewSet):
    queryset = QuizTaker.objects.all()
    serializer_class = QuizTakerSerializer


class UsersResponseViewSet(viewsets.ModelViewSet):
    queryset = UsersResponse.objects.all()
    serializer_class = UsersResponseSerializer
