from django.urls import path, include
from rest_framework.routers import DefaultRouter

from knowledge.views import (
    KnowledgeList,
    KnowledgeListWithPagination,
    KnowledgeCreate,
    KnowledgeDetailRetrieve,
    KnowledgeDetailUpdate,
    KnowledgeDetailDestroy,
)

urlpatterns = [
    path("", KnowledgeListWithPagination.as_view(), name="knowledge-list"),
    path("all/", KnowledgeList.as_view(), name="knowledge-list"),
    path(
        "create/",
        KnowledgeCreate.as_view(),
        name="knowledge-create",
    ),
    path(
        "<slug:slug>/",
        KnowledgeDetailRetrieve.as_view(),
        name="knowledge-detail-retrieve",
    ),
    path(
        "<slug:slug>/update/",
        KnowledgeDetailUpdate.as_view(),
        name="knowledge-detail-update",
    ),
    path(
        "<slug:slug>/destroy/",
        KnowledgeDetailDestroy.as_view(),
        name="knowledge-detail-destroy",
    ),
]
