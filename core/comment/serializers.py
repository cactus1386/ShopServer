from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True, source="author.username")

    class Meta:
        model = Comment
        fields = ('author', 'content', 'created_at', 'username',)