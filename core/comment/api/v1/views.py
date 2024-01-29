from django.shortcuts import render
from ...models import Comment
from rest_framework import status, generics, permissions
from .serializers import CommentSerializer


# Create your views here.
class CommentsView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()