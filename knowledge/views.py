from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from general.models import Tag, GenreForUrl
from .models import Knowledge
from .serializers import (
    KnowledgeSerializerForCreateUpdate,
    KnowledgeSerializerForGet,
    KnowledgeSerializerForDestroy,
)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from accounts.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework import status
from general.models import Language


class KnowledgeListWithPagination(generics.ListAPIView):
    queryset = Knowledge.objects.filter(language__name="en", type="knowledge")
    serializer_class = KnowledgeSerializerForGet
    permission_classes = [IsAdminOrReadOnly]
    paginate_by = 30


class KnowledgeListWithPaginationJp(generics.ListAPIView):
    queryset = Knowledge.objects.filter(language__name="jp", type="knowledge")
    serializer_class = KnowledgeSerializerForGet
    permission_classes = [IsAdminOrReadOnly]
    paginate_by = 30


class KnowledgeList(generics.ListAPIView):
    queryset = Knowledge.objects.filter(language__name="en", type="knowledge")
    serializer_class = KnowledgeSerializerForGet
    permission_classes = [IsAdminOrReadOnly]


class KnowledgeListJp(generics.ListAPIView):
    queryset = Knowledge.objects.filter(language__name="jp", type="knowledge")
    serializer_class = KnowledgeSerializerForGet
    permission_classes = [IsAdminOrReadOnly]


class KnowledgeDetailRetrieve(generics.RetrieveAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class KnowledgeDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class KnowledgeCreate(generics.CreateAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializerForCreateUpdate
    permission_classes = [AllowAny]


class KnowledgeDetailDestroy(generics.DestroyAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]
