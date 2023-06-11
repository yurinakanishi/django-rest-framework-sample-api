from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from general.models import Tag, Genre
from .models import Knowledge
from .serializers import (
    KnowledgeSerializer,
)

from api.permissions import AdminOrReadOnly
from rest_framework.permissions import AllowAny


class KnowledgeList(generics.ListAPIView):
    queryset = Knowledge.objects
    serializer_class = KnowledgeSerializer


class KnowledgeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Knowledge.objects
    serializer_class = KnowledgeSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class KnowledgeCreate(generics.CreateAPIView):
    queryset = Knowledge.objects
    serializer_class = KnowledgeSerializer
    lookup_field = "slug"
