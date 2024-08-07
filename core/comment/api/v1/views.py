from ...models import Comment
from .serializers import CommentSerializer
from rest_framework import generics
from rest_framework.response import Response


class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        pst = self.request.GET.get('pst')
        if pst:
            qs = qs.filter(post=pst)

        return qs

    def perform_create(self, serializer):
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({'invalid': 'bad request'})
