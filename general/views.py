from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Article, Tag, GenreForUrl
from .serializers import (
    ArticleSerializer,
    GenreForUrlSerializer,
    TagSerializer,
)

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from accounts.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework import status


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminOrReadOnly]


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class ArticleCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [IsAdminOrReadOnly]
    permission_classes = [AllowAny]


class GenreList(generics.ListAPIView):
    queryset = GenreForUrl.objects.all()
    serializer_class = GenreForUrlSerializer
    permission_classes = [IsAdminOrReadOnly]


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GenreForUrl.objects.all()
    serializer_class = GenreForUrlSerializer
    lookup_field = "name"
    permission_classes = [IsAdminOrReadOnly]


class GenreCreate(generics.CreateAPIView):
    queryset = GenreForUrl.objects.all()
    serializer_class = GenreForUrlSerializer
    # permission_classes = [IsAdminOrReadOnly]
    permission_classes = [AllowAny]


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrReadOnly]


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "name"
    permission_classes = [IsAdminOrReadOnly]


class TagCreate(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # permission_classes = [IsAdminOrReadOnly]
    permission_classes = [AllowAny]


@api_view(["GET", "POST"])
def genres_bulk_create(request):
    if request.method == "GET":
        knowledge = GenreForUrl.objects.all()
        serializers = GenreForUrlSerializer(knowledge, many=True)
        return Response(serializers.data)

    elif request.method == "POST":
        serializer = GenreForUrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
