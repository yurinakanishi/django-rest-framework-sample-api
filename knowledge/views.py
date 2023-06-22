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


# class KnowledgeList(generics.ListAPIView):
#     queryset = Knowledge.objects.all()
#     serializer_class = KnowledgeSerializer
#     permission_classes = [IsAdminOrReadOnly]
#     paginate_by = 30


# class KnowledgeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Knowledge.objects.all()
#     serializer_class = KnowledgeSerializer
#     lookup_field = "slug"
#     permission_classes = [IsAdminOrReadOnly]


# class KnowledgeCreate(generics.CreateAPIView):
#     queryset = Knowledge.objects.all()
#     serializer_class = KnowledgeSerializer
#     lookup_field = "slug"
#     permission_classes = [IsAdminUser]


class KnowledgeList(generics.ListAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializer
    permission_classes = [AllowAny]
    paginate_by = 30


class KnowledgeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class KnowledgeCreate(generics.CreateAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]
