from rest_framework import serializers
from .models import Quiz, Question, Response, Results


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'name', 'description', 'slug', 'roll_out', 'timestamp')


class ResponseSerializer(serializers.ModelSerializer):
    question_label = serializers.ReadOnlyField(
        source='question.label', read_only=True)
    class Meta:
        model = Response
        fields = ('id', 'question', 'label', 'carbon_output', 'question_label')


class QuestionSerializer(serializers.ModelSerializer):
    responses = ResponseSerializer(
        read_only=True,
        many=True
    )
    class Meta:
        model = Question
        fields = ('id', 'quiz', 'label', 'description',
                  'order',  'responses')


class ResultsSerializer(serializers.ModelSerializer):
    many = True
    class Meta:
        model = Results
        fields = ('id', 'carbon_output', 'owner', 'timestamp')
