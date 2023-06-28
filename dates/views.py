from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from general.models import Tag, GenreForURL
from .models import Period
from .serializers import (
    PeriodSerializer,
)

from accounts.permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAdminUser


class PeriodList(generics.ListAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    permission_classes = [IsAdminOrReadOnly]


class PeriodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Period.objects
    serializer_class = PeriodSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class PeriodCreate(generics.CreateAPIView):
    queryset = Period.objects
    serializer_class = PeriodSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]
