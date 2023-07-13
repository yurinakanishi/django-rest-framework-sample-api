from django.urls import path, include
from rest_framework.routers import DefaultRouter

from knowledge.views import (
    KnowledgeList,
    KnowledgeListJp,
    KnowledgeListWithPagination,
    KnowledgeListWithPaginationJp,
    KnowledgeCreate,
    KnowledgeDetailRetrieve,
    KnowledgeDetailUpdate,
    KnowledgeDetailDestroy,
)

urlpatterns = [
    path("", KnowledgeListWithPagination.as_view(), name="knowledge-list-jp"),
    path("jp/", KnowledgeListWithPaginationJp.as_view(), name="knowledge-list-jp"),
    path("all/", KnowledgeList.as_view(), name="knowledge-list-all-jp"),
    path("jp/all/", KnowledgeListJp.as_view(), name="knowledge-list-all-jp"),
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
