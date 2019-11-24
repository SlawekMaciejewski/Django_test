from django.shortcuts import get_object_or_404
from rest_framework import generics, views
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Post, Comment
from .serializers import PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AddCommentView(views.APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, name, email, content):
        post = get_object_or_404(Post, pk=pk)
        comment = Comment(name=name, email=email, content=content, active=True, post=post)
        comment.save()
        return Response({'added': True})




