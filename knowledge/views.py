from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from general.models import Tag, GenreForURL
from .models import Knowledge
from .serializers import KnowledgeSerializerForCreateUpdate, KnowledgeSerializerForGet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from accounts.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework import status

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


class KnowledgeListWithPagination(generics.ListAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializerForGet
    permission_classes = [AllowAny]
    paginate_by = 30


class KnowledgeList(generics.ListAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializerForGet
    permission_classes = [AllowAny]


class KnowledgeDetailRetrieve(generics.RetrieveAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializerForGet
    lookup_field = "slug"
    permission_classes = [AllowAny]


class KnowledgeDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [AllowAny]


class KnowledgeCreate(generics.CreateAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializerForCreateUpdate
    permission_classes = [AllowAny]


class KnowledgeDetailDestroy(generics.DestroyAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [AllowAny]
