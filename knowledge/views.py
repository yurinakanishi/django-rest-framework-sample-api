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
    KnowledgeSearchSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from accounts.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework import status
from general.models import Language
from django.shortcuts import get_list_or_404


class BaseKnowledgeList(generics.ListAPIView):
    serializer_class = KnowledgeSerializerForGet
    permission_classes = [IsAdminOrReadOnly]

    def get_custom_queryset(self):
        lang = self.request.GET.get("lang", "en")
        author_id = self.request.GET.get("user-id")
        type = self.kwargs.get("type", "each")

        if type == "test":
            query = Knowledge.objects.filter(
                language__name=lang, type__in=["each", "test"]
            )
        else:
            query = Knowledge.objects.filter(language__name=lang, type=type)

        if author_id:
            query = query.filter(author__id=author_id)

        return query.order_by("-article__published_date")


class KnowledgeListWithPagination(BaseKnowledgeList):
    paginate_by = 30

    def get_queryset(self):
        return self.get_custom_queryset()


class KnowledgeList(BaseKnowledgeList):
    def get_queryset(self):
        return self.get_custom_queryset()


class KnowledgeSearchList(generics.ListAPIView):
    serializer_class = KnowledgeSearchSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_language_queryset(self):
        lang = self.request.GET.get("lang", "en")
        type = self.kwargs.get("type", "each")
        return Knowledge.objects.filter(language__name=lang)


class KnowledgeDetailRetrieve(generics.RetrieveAPIView):
    serializer_class = KnowledgeSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        # Start with all Knowledge objects.
        queryset = Knowledge.objects.all()
        type = self.kwargs.get("type", "each")
        # Get the lang parameter from the request's GET dictionary.
        lang = self.request.query_params.get("lang", None)

        # Filter the Knowledge objects by the lang parameter if it's present.
        if lang:
            queryset = queryset.filter(language=lang, type=type)

        return queryset

    def get_object(self):
        # Override the get_object method to use the filtered queryset.
        queryset = self.filter_queryset(self.get_queryset())

        # Look up the object by the 'slug' lookup_field.
        obj = get_object_or_404(
            queryset, **{self.lookup_field: self.kwargs[self.lookup_field]}
        )

        # Check object permissions.
        self.check_object_permissions(self.request, obj)

        return obj


class KnowledgeDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [AllowAny]


class KnowledgeCreate(generics.CreateAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializerForCreateUpdate
    permission_classes = [IsAuthenticated]


class KnowledgeDetailDestroy(generics.DestroyAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]
