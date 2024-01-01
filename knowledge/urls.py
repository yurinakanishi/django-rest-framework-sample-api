from django.urls import path, include
from rest_framework.routers import DefaultRouter

from knowledge.views import (
    KnowledgeList,
    KnowledgeListWithPagination,
    KnowledgeCreate,
    KnowledgeDetailRetrieve,
    KnowledgeDetailUpdate,
    KnowledgeDetailDestroy,
    KnowledgeSearchList,
)

urlpatterns = [
    path(
        "<str:type>/with-pagination/",
        KnowledgeListWithPagination.as_view(),
        name="knowledge-list-with-pagination",
    ),
    path("<str:type>/all/", KnowledgeList.as_view(), name="knowledge-list-all"),
    path(
        "search/",
        KnowledgeSearchList.as_view(),
        name="knowledge-search",
    ),
    path(
        "create/",
        KnowledgeCreate.as_view(),
        name="knowledge-create",
    ),
    path(
        "<str:type>/<slug:slug>/",
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
