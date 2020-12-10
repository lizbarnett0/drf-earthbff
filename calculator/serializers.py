from rest_framework import serializers
from .models import Quiz, Question, Response, QuizTaker, UsersResponse


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'name', 'description', 'slug', 'roll_out', 'timestamp')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'quiz', 'label', 'order')


class ResponseSerializer(serializers.ModelSerializer):
    question_label = serializers.ReadOnlyField(
            source='question.label', read_only=True)
    class Meta:
        model = Response
        fields = ('id', 'question', 'label', 'carbon_output', 'question_label')


class QuizTakerSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(
            source='users.User.email', read_only=True)
    quiz_name = serializers.ReadOnlyField(
            source='quiz.name', read_only=True)
    class Meta:
        model = QuizTaker
        fields = ('id', 'user', 'quiz', 'carbon_footprint', 'completed', 'date_finished', 'timestamp', 'user_email', 'quiz_name')


class UsersResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersResponse
        fields = ('id', 'quiz_taker', 'question', 'response')
