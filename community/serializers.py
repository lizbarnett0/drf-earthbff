from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'body', 'post', 'timestamp')

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(
        read_only=True,
        many=True
    )
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'timestamp', 'comments')
