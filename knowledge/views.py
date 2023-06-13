from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from general.models import Tag, Genre
from .models import Knowledge
from .serializers import (
    KnowledgeSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from api.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly


class KnowledgeList(generics.ListAPIView):
    queryset = Knowledge.objects
    serializer_class = KnowledgeSerializer
    permission_classes = [IsAdminOrReadOnly]


class KnowledgeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Knowledge.objects
    serializer_class = KnowledgeSerializer
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class KnowledgeCreate(generics.CreateAPIView):
    queryset = Knowledge.objects
    serializer_class = KnowledgeSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]
